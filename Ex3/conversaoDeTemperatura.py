import json

from dotenv import load_dotenv
from groq import Groq

from tools import celsius_para_fahrenheit, fahrenheit_para_celsius

load_dotenv()

client = Groq()

tools = [
	{
		"type": "function",
		"function": {
			"name": "celsius_para_fahrenheit",
			"description": "Converte uma temperatura em Celsius para Fahrenheit.",
			"parameters": {
				"type": "object",
				"properties": {
					"temperatura": {
						"type": "number",
						"description": "Valor da temperatura em graus Celsius"
					}
				},
				"required": ["temperatura"]
			}
		}
	},
	{
		"type": "function",
		"function": {
			"name": "fahrenheit_para_celsius",
			"description": "Converte uma temperatura em Fahrenheit para Celsius.",
			"parameters": {
				"type": "object",
				"properties": {
					"temperatura": {
						"type": "number",
						"description": "Valor da temperatura em graus Fahrenheit"
					}
				},
				"required": ["temperatura"]
			}
		}
	}
]

function_map = {
	"celsius_para_fahrenheit": celsius_para_fahrenheit,
	"fahrenheit_para_celsius": fahrenheit_para_celsius,
}


def perguntar(pergunta: str):
	response = client.chat.completions.create(
		model="openai/gpt-oss-120b",
		messages=[
			{
				"role": "system",
				"content": "Você é um assistente que escolhe a função correta de conversão de temperatura. Use celsius_para_fahrenheit para Celsius -> Fahrenheit e fahrenheit_para_celsius para Fahrenheit -> Celsius."
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
	print(perguntar("Converter 30 graus Celsius para Fahrenheit"))
	print(perguntar("Quanto é 80F em Celsius?"))
