import json

from dotenv import load_dotenv
from groq import Groq

from tools import buscar_clima

load_dotenv()

client = Groq()

tools = [
    {
        "type": "function",
        "function": {
            "name": "buscar_clima",
            "description": (
                "Consulta o clima de uma cidade com base no nome informado."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "cidade": {
                        "type": "string",
                        "description": "Nome da cidade para consultar o clima"
                    }
                },
                "required": ["cidade"]
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
                "content": (
                    "Você é um assistente que escolhe a função correta para "
                    "consultar o clima de cidades. Sempre use buscar_clima "
                    "quando o usuário pedir clima, temperatura, previsão do "
                    "tempo ou como está o tempo."
                )
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

        if tool_name == "buscar_clima":
            return buscar_clima(**args)

    return message.content


if __name__ == "__main__":
    print(perguntar("Como está o clima em Bauru?"))
    print(perguntar("Qual a temperatura em Curitiba?"))