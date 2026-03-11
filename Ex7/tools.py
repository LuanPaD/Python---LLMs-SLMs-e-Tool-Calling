def buscar_clima(cidade: str):
    clima = {
        "sao paulo": "24°C e nublado",
        "bauru": "30°C e ensolarado",
        "curitiba": "18°C e chuvoso"
    }

    chave = cidade.lower().strip()
    previsao = clima.get(chave)

    if previsao:
        return f"O clima em {cidade.title()} está {previsao}."

    return f"Não encontrei dados de clima para {cidade.title()}."
