"""Funções simples usadas para aprender integração contínua."""


def add(a: int, b: int) -> int:
    return a + b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("divisor cannot be zero")
    return a / b
