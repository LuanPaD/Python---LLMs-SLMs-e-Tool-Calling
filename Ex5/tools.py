def buscar_produto(produto: str):
    estoque = {
        "notebook": 5,
        "mouse": 20,
        "teclado": 8
    }

    if produto in estoque:
        return f"Sim, temos {produto} em estoque."
    
    return f"{produto} não encontrado no estoque."


def verificar_estoque(produto: str):
    estoque = {
        "notebook": 5,
        "mouse": 20,
        "teclado": 8
    }

    quantidade = estoque.get(produto)

    if quantidade is not None:
        return f"Temos {quantidade} {produto}(s) em estoque."
    
    return f"{produto} não encontrado no estoque."