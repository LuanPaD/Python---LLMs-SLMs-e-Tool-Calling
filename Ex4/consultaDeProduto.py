"""
Exercício 4 — Consulta de Produto
O sistema interpreta mensagens e busca o preço de um produto.
"""

import json
from groq import Groq
from dotenv import load_dotenv
from tools import buscar_produto

load_dotenv()

client = Groq()

tools = [
    {
        "type": "function",
        "function": {
            "name": "buscar_produto",
            "description": "Busca o preço de um produto pelo nome",
            "parameters": {
                "type": "object",
                "properties": {
                    "nome_produto": {
                        "type": "string",
                        "description": "Nome do produto a ser consultado (ex: notebook, mouse, teclado)"
                    }
                },
                "required": ["nome_produto"]
            }
        }
    }
]

def perguntar(pergunta: str):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "Você é um assistente de loja. Interprete a mensagem e consulte o preço do produto solicitado."},
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

    return message.content


print(perguntar("Qual o preço do notebook?"))
print(perguntar("Quanto custa um mouse?"))
