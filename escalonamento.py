
EPSILON = 1e-10


""" funçao para veficar se a matriz é quadrada """
def matriz_valida(matriz) -> bool:
    
    colunas_matriz = len(matriz[0])
    
    for linha in matriz:
        if len(linha) != colunas_matriz:
            return False
    
    return True
        



""" função para verificar o tipo do sistema linear"""
def tipo_sistema(matriz) -> str:
    # pega o numero de equacoes
    m = len(matriz)
    # numero de incognitas - 1 da coluna final
    n = len(matriz[0]) - 1


    if (m > n):
        return "superdeterminado"
    elif (m < n):
        return "subdeterminado"
    else:
        return "determinado"
    
""" função para trocar linhas"""
def trocar_linhas(matriz, linha_a, linha_b):
    matriz[linha_a], matriz[linha_b] =  matriz[linha_b], matriz[linha_a]
    
""" função para encontrar a linha do maior pivô"""
def encontrar_pivo(matriz, linha_inicio, coluna):
    
    linha_pivo = None
    maior_valor = 0
    
    for linha in range(linha_inicio, len(matriz)):
        valor = abs(matriz[linha][coluna])
        
        if valor > maior_valor:
            maior_valor = valor
            linha_pivo = linha
    
    # por estar trabalhando com float, ha chance de encontrar um numero como 0.00000001 que seria um caso diferente de != 0
    if maior_valor < EPSILON:
        return None
    
    return linha_pivo
""" funçao para fazer eliminaçao de gauss"""
def eliminar_abaixo(matriz, linha_pivo, coluna_pivo):
    pivo = matriz[linha_pivo][coluna_pivo]

    for linha in range(linha_pivo + 1, len(matriz)):
        elemento = matriz[linha][coluna_pivo]

        if abs(elemento) < EPSILON:
            continue

        fator = elemento / pivo

        for coluna in range(coluna_pivo, len(matriz[linha])):
            matriz[linha][coluna] -= fator * matriz[linha_pivo][coluna]

        matriz[linha][coluna_pivo] = 0.0

"""funçao para realizar o escalonamento em todo o sistema linear"""
def escalonar(matriz):
    if not matriz_valida(matriz):
        raise ValueError("Matriz inválida.")

    numero_linhas = len(matriz)
    numero_incognitas = len(matriz[0]) - 1

    linha_pivo = 0

    for coluna_pivo in range(numero_incognitas):

        if linha_pivo >= numero_linhas:
            break

        linha_encontrada = encontrar_pivo(
            matriz,
            linha_pivo,
            coluna_pivo
        )

        if linha_encontrada is None:
            continue

        if linha_encontrada != linha_pivo:
            trocar_linhas(
                matriz,
                linha_pivo,
                linha_encontrada
            )

        eliminar_abaixo(
            matriz,
            linha_pivo,
            coluna_pivo
        )

        linha_pivo += 1

    return matriz