import re
import unicodedata

from tools import buscar_clima


def remover_acentos(texto: str):
    return "".join(
        caractere
        for caractere in unicodedata.normalize("NFD", texto)
        if unicodedata.category(caractere) != "Mn"
    )


def extrair_cidade(mensagem: str):
    mensagem_normalizada = remover_acentos(mensagem.lower()).strip()

    padroes = [
        r"clima em\s+([a-z\s]+)",
        r"temperatura em\s+([a-z\s]+)",
    ]

    for padrao in padroes:
        resultado = re.search(padrao, mensagem_normalizada)
        if resultado:
            cidade = resultado.group(1).strip(" ?!.,")
            return cidade

    return None


def perguntar(mensagem: str):
    cidade = extrair_cidade(mensagem)

    if cidade:
        return buscar_clima(cidade)

    return "Não consegui identificar a cidade na sua mensagem."


if __name__ == "__main__":
    print(perguntar("Como está o clima em Bauru?"))
    print(perguntar("Qual a temperatura em Curitiba?"))
