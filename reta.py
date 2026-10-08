# import apenas para visualizar 
import matplotlib.pyplot as plt
import matplotlib

# tive que trocar o modelo do backend pra rodar no linux, entao ignore essa linha
matplotlib.use("TkAgg")

EPSILON = 1e-10


def validar_ponto_vetor(ponto, vetor):
    if len(ponto) != len(vetor):
        raise ValueError("O ponto e o vetor devem possuir a mesma dimensão.")

    if len(ponto) not in (2, 3):
        raise ValueError("A reta deve estar em R² ou R³.")

    vetor_nulo = True

    for componente in vetor:
        if abs(componente) > EPSILON:
            vetor_nulo = False
            break

    if vetor_nulo:
        raise ValueError("O vetor diretor não pode ser o vetor nulo.")

def equacao_vetorial(ponto, vetor):
    validar_ponto_vetor(ponto, vetor)

    ponto_texto = ", ".join(str(valor) for valor in ponto)
    vetor_texto = ", ".join(str(valor) for valor in vetor)

    return (f"({ponto_texto}) + t({vetor_texto})") 

def equacoes_parametricas(ponto, vetor):
    validar_ponto_vetor(ponto, vetor)

    nomes_variaveis = ["x", "y", "z"]

    equacoes = []

    for i in range(len(ponto)):
        equacao = (
            f"{nomes_variaveis[i]} = "
            f"{ponto[i]} + ({vetor[i]})t"
        )

        equacoes.append(equacao)

    return equacoes

def gerar_pontos_reta(
    ponto,
    vetor,
    inicio=-10,
    fim=10,
    quantidade=100
):
    validar_ponto_vetor(ponto, vetor)

    valores_t = []

    passo = (fim - inicio) / (quantidade - 1)

    for i in range(quantidade):
        t = inicio + i * passo
        valores_t.append(t)

    coordenadas = []

    for _ in range(len(ponto)):
        coordenadas.append([])

    for t in valores_t:

        for dimensao in range(len(ponto)):

            valor = (ponto[dimensao]+ t * vetor[dimensao])

            coordenadas[dimensao].append(valor)

    return coordenadas

        
def plotar_reta_2d(ponto, coordenadas):
    xs = coordenadas[0]
    ys = coordenadas[1]

    plt.figure()

    plt.plot(
        xs,
        ys,
        label="Reta"
    )

    plt.scatter(
        ponto[0],
        ponto[1],
        label="Ponto P"
    )

    plt.axhline(0)
    plt.axvline(0)

    plt.xlabel("x")
    plt.ylabel("y")

    plt.grid()

    plt.legend()

    plt.show()
    
def plotar_reta_3d(ponto, coordenadas):
    xs = coordenadas[0]
    ys = coordenadas[1]
    zs = coordenadas[2]

    fig = plt.figure()

    ax = fig.add_subplot(
        111,
        projection="3d"
    )

    ax.plot(
        xs,
        ys,
        zs,
        label="Reta"
    )

    ax.scatter(
        ponto[0],
        ponto[1],
        ponto[2],
        label="Ponto P"
    )

    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")

    ax.legend()

    plt.show()
    
def plotar_reta(ponto, vetor):
    validar_ponto_vetor(ponto, vetor)

    coordenadas = gerar_pontos_reta(
        ponto,
        vetor
    )

    if len(ponto) == 2:
        plotar_reta_2d(
            ponto,
            coordenadas
        )

    else:
        plotar_reta_3d(
            ponto,
            coordenadas
        )
        
