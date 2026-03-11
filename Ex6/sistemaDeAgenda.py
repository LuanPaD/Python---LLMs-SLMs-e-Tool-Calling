import json

from dotenv import load_dotenv
from groq import Groq

from tools import criar_evento, listar_eventos

load_dotenv()

client = Groq()

tools = [
	{
		"type": "function",
		"function": {
			"name": "criar_evento",
			"description": "Cria um evento na agenda com titulo e data.",
			"parameters": {
				"type": "object",
				"properties": {
					"titulo": {
						"type": "string",
						"description": "Título do evento"
					},
					"data": {
						"type": "string",
						"description": "Data do evento"
					}
				},
				"required": ["titulo", "data"]
			}
		}
	},
	{
		"type": "function",
		"function": {
			"name": "listar_eventos",
			"description": "Mostra todos os eventos cadastrados na agenda.",
			"parameters": {
				"type": "object",
				"properties": {}
			}
		}
	}
]


def perguntar(pergunta: str):
	response = client.chat.completions.create(
		model="openai/gpt-oss-120b",
		messages=[
			{
				"role": "system",
				"content": "Você é um assistente que escolhe a função correta da agenda. Se o usuário pedir para criar, cadastrar ou adicionar evento, use criar_evento. Se pedir para mostrar, listar ou ver eventos, use listar_eventos."
			},
			{"role": "user", "content": pergunta}
		],
		tools=tools,
		tool_choice="auto",
		temperature=0
	)

	message = response.choices[0].message

	if message.tool_calls:
		tool_call = message.tool_calls[0]
		tool_name = tool_call.function.name
		args = json.loads(tool_call.function.arguments)

		print(f"Função chamada: {tool_name}")
		print(f"Argumentos: {args}")

		if tool_name == "criar_evento":
			return criar_evento(**args)

		if tool_name == "listar_eventos":
			return listar_eventos()

	return message.content


if __name__ == "__main__":
	print(perguntar("Criar evento reunião amanhã"))
	print(perguntar("Mostrar meus eventos"))
