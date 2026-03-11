import os
import json
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq()

# Base de dados
estoque = {
    "notebook": 5,
    "mouse": 20,
    "teclado": 8
}

# Funções do sistema
def buscar_produto(produto: str):
    if produto in estoque:
        return f"Sim, temos {produto} em estoque."
    else:
        return f"Não encontramos {produto} no estoque."

def verificar_estoque(produto: str):
    quantidade = estoque.get(produto, 0)
    return f"Temos {quantidade} {produto}(s) em estoque."

# Definição das tools
tools = [
    {
        "type": "function",
        "function": {
            "name": "buscar_produto",
            "description": "Verifica se um produto existe no estoque",
            "parameters": {
                "type": "object",
                "properties": {
                    "produto": {
                        "type": "string",
                        "description": "Nome do produto"
                    }
                },
                "required": ["produto"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "verificar_estoque",
            "description": "Retorna a quantidade disponível de um produto",
            "parameters": {
                "type": "object",
                "properties": {
                    "produto": {
                        "type": "string",
                        "description": "Nome do produto"
                    }
                },
                "required": ["produto"]
            }
        }
    }
]

def perguntar(pergunta: str):
    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {"role": "system", "content": "Você é um assistente que decide qual função usar para consultar o estoque."},
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

        print(f"Tool chamada: {tool_name}")
        print(f"Argumentos: {args}")

        if tool_name == "buscar_produto":
            return buscar_produto(**args)

        if tool_name == "verificar_estoque":
            return verificar_estoque(**args)

    return message.content


print(perguntar("Tem notebook em estoque?"))
print(perguntar("Quantos mouse temos?"))