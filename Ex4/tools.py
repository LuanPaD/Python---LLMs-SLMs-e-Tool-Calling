produtos = {
    "notebook": 4500,
    "mouse": 80,
    "teclado": 150
}

def buscar_produto(nome_produto: str):
    chave = nome_produto.lower().strip()
    if chave in produtos:
        return f"O preço do {nome_produto} é R$ {produtos[chave]:.2f}."
    return f"Produto '{nome_produto}' não encontrado."
