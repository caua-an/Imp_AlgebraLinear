from escalonamento import EPSILON, matriz_valida

""" funçao para retornar a posicao dos pivos"""
def identificar_pivos(matriz):
    pivos = []

    numero_incognitas = len(matriz[0]) - 1

    for indice_linha, linha in enumerate(matriz):

        for coluna in range(numero_incognitas):

            if abs(linha[coluna]) > EPSILON:
                pivos.append(
                    (indice_linha, coluna)
                )

                break

    return pivos

""" funçao para localizar variaveis livres na matriz"""
def identificar_variaveis_livres(matriz):
    numero_incognitas = len(matriz[0]) - 1

    pivos = identificar_pivos(matriz)

    colunas_pivo = []

    for _, coluna in pivos:
        colunas_pivo.append(coluna)

    variaveis_livres = []

    for coluna in range(numero_incognitas):
        if coluna not in colunas_pivo:
            variaveis_livres.append(coluna)

    return variaveis_livres

""" funçao para encontrar inconsistencias como 0x + 0y = 2"""
def tem_inconsistencia(matriz):
    numero_incognitas = len(matriz[0]) - 1

    for linha in matriz:

        coeficientes_zerados = True

        for coluna in range(numero_incognitas):
            if abs(linha[coluna]) > EPSILON:
                coeficientes_zerados = False
                break

        termo_independente = linha[-1]

        if (
            coeficientes_zerados
            and abs(termo_independente) > EPSILON
        ):
            return True

    return False

""" funcao para retornar o posto do sistema"""
def calcular_posto(matriz):
    return len(
        identificar_pivos(matriz)
    )

""" funcao principal da analise de um sistema sobre quantas soluções ele possui"""
def classificar_solucao(matriz):
    if not matriz_valida(matriz):
        raise ValueError("Matriz inválida.")

    if tem_inconsistencia(matriz):
        return "sem_solucao"

    numero_incognitas = len(matriz[0]) - 1

    posto = calcular_posto(matriz)

    if posto == numero_incognitas:
        return "solucao_unica"

    return "infinitas_solucoes"