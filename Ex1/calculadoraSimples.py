# import os
import json
from groq import Groq
from tools import somar, multiplicar

# conseguir ler o arquivo .env para pegar a chave da API
from dotenv import load_dotenv

load_dotenv()

client = Groq()


# configurar o groq para usar as funções de soma e multiplicação
# Define as ferramentas disponíveis para o assistente, permitindo que ele chame funções específicas
tools = [
    {
        "type": "function",
        "function": {
            "name": "somar",
            "description": "Soma dois números",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {
                        "type": "number",
                        "description": "Primeiro número"
                    },
                    "b": {
                        "type": "number",
                        "description": "Segundo número"
                    }
                },
                "required": ["a", "b"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "multiplicar",
            "description": "Multiplica dois números",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {
                        "type": "number",
                        "description": "Primeiro número"
                    },
                    "b": {
                        "type": "number",
                        "description": "Segundo número"
                    }
                },
                "required": ["a", "b"]
            }
        }
    }
]

# Função principal que processa a pergunta do usuário, decide qual ferramenta usar e retorna o resultado
def perguntar(pergunta: str):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "Você é um assistente que decide qual função usar para calcular."},
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

        print(f"Operação: {tool_name}")
        print(f"Números: {args}")

        if tool_name == "somar":
            return somar(**args)

        if tool_name == "multiplicar":
            return multiplicar(**args)

    return message.content

# Exemplos de uso
print(perguntar("Quanto é 5 + 3?"))
print(perguntar("Multiplique 4 por 7"))
