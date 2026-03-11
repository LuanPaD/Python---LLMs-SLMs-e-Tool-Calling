import unicodedata


def normalizar_texto(texto: str):
    texto_sem_acentos = "".join(
        caractere
        for caractere in unicodedata.normalize("NFD", texto.lower())
        if unicodedata.category(caractere) != "Mn"
    )
    return " ".join(texto_sem_acentos.strip().split())


def buscar_clima(cidade: str):
    clima = {
        "sao paulo": "24°C e nublado",
        "bauru": "30°C e ensolarado",
        "curitiba": "18°C e chuvoso"
    }

    chave = normalizar_texto(cidade)
    previsao = clima.get(chave)

    if previsao:
        return f"O clima em {cidade.title()} está {previsao}."

    return f"Não encontrei dados de clima para {cidade.title()}."