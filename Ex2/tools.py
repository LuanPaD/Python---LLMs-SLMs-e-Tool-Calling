def somar(numero1: float, numero2: float):
    return numero1 + numero2


def subtrair(numero1: float, numero2: float):
    return numero1 - numero2


def multiplicar(numero1: float, numero2: float):
    return numero1 * numero2


def dividir(numero1: float, numero2: float):
    if numero2 == 0:
        return "Não é possível dividir por zero."

    return numero1 / numero2