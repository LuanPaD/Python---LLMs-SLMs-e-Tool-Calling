import json

from dotenv import load_dotenv
from groq import Groq

from tools import somar, subtrair, multiplicar, dividir

load_dotenv()

client = Groq()

tools = [
	{
		"type": "function",
		"function": {
			"name": "somar",
			"description": "Soma dois números. Use para pedidos com mais, soma, adição ou total.",
			"parameters": {
				"type": "object",
				"properties": {
					"numero1": {
						"type": "number",
						"description": "Primeiro número da soma"
					},
					"numero2": {
						"type": "number",
						"description": "Segundo número da soma"
					}
				},
				"required": ["numero1", "numero2"]
			}
		}
	},
	{
		"type": "function",
		"function": {
			"name": "subtrair",
			"description": "Subtrai dois números. Use para pedidos com menos, subtração, diferença ou retirar.",
			"parameters": {
				"type": "object",
				"properties": {
					"numero1": {
						"type": "number",
						"description": "Número do qual algo será subtraído"
					},
					"numero2": {
						"type": "number",
						"description": "Número que será subtraído"
					}
				},
				"required": ["numero1", "numero2"]
			}
		}
	},
	{
		"type": "function",
		"function": {
			"name": "multiplicar",
			"description": "Multiplica dois números. Use para pedidos com vezes, multiplicação ou produto.",
			"parameters": {
				"type": "object",
				"properties": {
					"numero1": {
						"type": "number",
						"description": "Primeiro fator"
					},
					"numero2": {
						"type": "number",
						"description": "Segundo fator"
					}
				},
				"required": ["numero1", "numero2"]
			}
		}
	},
	{
		"type": "function",
		"function": {
			"name": "dividir",
			"description": "Divide dois números. Use para pedidos com dividido por, divisão, quociente ou repartir.",
			"parameters": {
				"type": "object",
				"properties": {
					"numero1": {
						"type": "number",
						"description": "Dividendo"
					},
					"numero2": {
						"type": "number",
						"description": "Divisor"
					}
				},
				"required": ["numero1", "numero2"]
			}
		}
	}
]

function_map = {
	"somar": somar,
	"subtrair": subtrair,
	"multiplicar": multiplicar,
	"dividir": dividir,
}


def perguntar(pergunta: str):
	response = client.chat.completions.create(
		model="openai/gpt-oss-120b",
		messages=[
			{
				"role": "system",
				"content": "Você é um assistente que decide qual operação matemática usar. Sempre escolha uma função quando o usuário pedir soma, subtração, multiplicação ou divisão."
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

		function = function_map.get(tool_name)
		if function:
			return function(**args)

	return message.content


if __name__ == "__main__":
	print(perguntar("Quanto é 10 dividido por 2?"))
	print(perguntar("Calcule 15 menos 8"))
	print(perguntar("Calcule 10 mais 8"))
	print(perguntar("Calcule 15 multiplicado por 8"))
