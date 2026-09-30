
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