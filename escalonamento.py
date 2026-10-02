
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
    maior_valor = None
    
    for linha in range(linha_inicio, len(matriz)):
        valor = abs(matriz[linha][coluna])
        
        if valor > maior_valor:
            linha_pivo = linha
    
    # por estar trabalhando com float, ha chance de encontrar um numero como 0.00000001 que seria um caso diferente de != 0
    if maior_valor < EPSILON:
        return None
    
    return linha_pivo