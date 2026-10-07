from escalonamento import EPSILON

from analise import (
    classificar_solucao,
    identificar_pivos,
    identificar_variaveis_livres
)

""" função para realizar uma retrosubstituiçao de um sistema linear, ja que possui apenas umas solução"""
def resolver_solucao_unica(matriz):

    if classificar_solucao(matriz) != "solucao_unica":
        raise ValueError("O sistema não possui solução única.")

    numero_incognitas = len(matriz[0]) - 1

    solucoes = [0.0] * numero_incognitas

    pivos = identificar_pivos(matriz)

    for linha_pivo, coluna_pivo in reversed(pivos):

        termo_independente = matriz[linha_pivo][-1]

        soma = 0.0

        for coluna in range(
            coluna_pivo + 1,
            numero_incognitas
        ):
            soma += (
                matriz[linha_pivo][coluna]
                * solucoes[coluna]
            )

        pivo = matriz[linha_pivo][coluna_pivo]

        solucoes[coluna_pivo] = (
            termo_independente - soma
        ) / pivo

        if abs(solucoes[coluna_pivo]) < EPSILON:
            solucoes[coluna_pivo] = 0.0

    return solucoes

""" função para resolver sistemas caso o número de pivôs seja maior que o número de variáveis livres"""
def resolver_infinitas_solucoes(matriz):

    if classificar_solucao(matriz) != "infinitas_solucoes":
        raise ValueError(
            "O sistema não possui infinitas soluções."
        )

    numero_incognitas = len(matriz[0]) - 1

    pivos = identificar_pivos(matriz)

    variaveis_livres = identificar_variaveis_livres(
        matriz
    )

    quantidade_parametros = len(variaveis_livres)

    solucoes = []

    for _ in range(numero_incognitas):
        # forma de representar uma expressao em casos em que há uma variavel livre,por exemplo, quando uma soluçao final se de por x= 3-t, y = 1 e z = t, em que z é a variável livre  
        # assim guardaria em x = 3 - t, constante:3 e parametros: -1
        solucoes.append({
            "constante": 0.0,
            "parametros": [0.0] * quantidade_parametros
        })

    for indice_parametro, coluna in enumerate(variaveis_livres):
        solucoes[coluna]["parametros"][indice_parametro] = 1.0

    
    # daqui pra frente é retrosubstituição usando a ideia da expressao guardada acima
    for linha_pivo, coluna_pivo in reversed(pivos):

        constante = matriz[linha_pivo][-1]

        parametros = [0.0] * quantidade_parametros

        for coluna in range(
            coluna_pivo + 1,
            numero_incognitas
        ):

            coeficiente = matriz[linha_pivo][coluna]

            if abs(coeficiente) < EPSILON:
                continue

            constante -= (
                coeficiente
                * solucoes[coluna]["constante"]
            )

            for i in range(quantidade_parametros):
                parametros[i] -= (
                    coeficiente
                    * solucoes[coluna]["parametros"][i]
                )

        pivo = matriz[linha_pivo][coluna_pivo]

        constante /= pivo

        for i in range(quantidade_parametros):
            parametros[i] /= pivo

        solucoes[coluna_pivo] = {
            "constante": constante,
            "parametros": parametros
        }

    return {
        "solucoes": solucoes,
        "variaveis_livres": variaveis_livres
    }

""" funçao para realizar uma fachada para resolver os sistemas """
def resolver_sistema(matriz):

    classificacao = classificar_solucao(matriz)

    if classificacao == "sem_solucao":
        return {
            "tipo": "sem_solucao",
            "solucao": None
        }

    if classificacao == "solucao_unica":
        return {
            "tipo": "solucao_unica",
            "solucao": resolver_solucao_unica(matriz)
        }

    return {
        "tipo": "infinitas_solucoes",
        "solucao": resolver_infinitas_solucoes(matriz)
    }