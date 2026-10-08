from escalonamento import escalonar, tipo_sistema
from analise import classificar_solucao
from solucao import resolver_sistema
from reta import (
    equacao_vetorial,
    equacoes_parametricas,
    plotar_reta
)


def mostrar_resultado(nome, matriz):
    print(f"\n===== {nome} =====")

    print("Tipo:", tipo_sistema(matriz))

    matriz_escalonada = escalonar(matriz)

    print("\nMatriz escalonada:")
    for linha in matriz_escalonada:
        print(linha)

    print("\nClassificação:")
    print(classificar_solucao(matriz_escalonada))

    print("\nResultado:")
    print(resolver_sistema(matriz_escalonada))


def main():

    matriz_1 = [
        [1.0, 1.0, 3.0],
        [2.0, -1.0, 0.0],
        [3.0, 0.0, 3.0]
    ]

    matriz_2 = [
        [1.0, 1.0, 3.0],
        [2.0, -1.0, 0.0],
        [1.0, 1.0, 10.0]
    ]

    matriz_3 = [
        [1.0, 1.0, 1.0, 4.0],
        [1.0, -1.0, 1.0, 2.0]
    ]

    mostrar_resultado(
        "Matriz 1 - Solução única",
        matriz_1
    )

    mostrar_resultado(
        "Matriz 2 - Sem solução",
        matriz_2
    )

    mostrar_resultado(
        "Matriz 3 - Infinitas soluções",
        matriz_3
    )

    ponto = (2.0, 3.0)
    vetor = (4.0, -1.0)

    print("\n===== RETA =====")

    print("\nEquação vetorial:")
    print(
        "(x, y) =",
        equacao_vetorial(ponto, vetor)
    )

    print("\nEquações paramétricas:")
    for equacao in equacoes_parametricas(
        ponto,
        vetor
    ):
        print(equacao)

    plotar_reta(
        ponto,
        vetor
    )


if __name__ == "__main__":
    main()