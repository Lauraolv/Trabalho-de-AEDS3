import time
import graph

def arq_lab(arquivo):
    with open(arquivo, "r") as labirinto:
        linhas = labirinto.read().splitlines()
    return linhas

def formar_grafo(labirinto):
    linha = len(labirinto)
    coluna = len(labirinto[0])
    indice = 0
    g1 = graph.Graph(linha * coluna, adj_list=[])
    for i in range(linha):
        for j in range(coluna):
            g1.nodes.append((i, j, labirinto[i][j]))
    for i in range(linha):
        for j in range(coluna):
            indice = (coluna * i) + j
            if i > 0 and labirinto[i][j] != "#" and labirinto[i-1][j] != "#":
                g1.add_directed_edge(indice, ((coluna * (i - 1) + j)))
            if i + 1 < linha and labirinto[i][j] != "#" and labirinto[i+1][j] != "#":
                g1.add_directed_edge(indice, (coluna * (i + 1) + j))
            if j > 0 and labirinto[i][j-1] != "#" and labirinto[i][j]!= "#":
                g1.add_directed_edge(indice, (coluna * i) + (j - 1))
            if j + 1 < coluna and labirinto[i][j] != "#" and labirinto[i][j + 1] != "#":
                g1.add_directed_edge(indice, (coluna * i) + (j + 1))  
    return g1



def encontrar_caminho(g1, labirinto):
    linha = len(labirinto)
    coluna = len(labirinto[0])
    for i in range(linha):
        for j in range(coluna):
            indice = (coluna * i) + j
            if labirinto[i][j] == "S":
                inicio = indice
            if labirinto[i][j] == "E":
                fim = indice
    caminho = g1.dfs(inicio, fim)
    return(caminho)
    
def no_arestas(caminho, g1, labirinto):
    linha = len(labirinto)
    coluna = len(labirinto[0])
    arestas = []
    for e in caminho:
        u,v, _ = g1.nodes[e]
        arestas.append((u,v))

    return (arestas)

def labirinto(arquivo):
    lab = arq_lab(arquivo)
    g1 = formar_grafo(lab)
    # g1.imprime()
    inicio = time.time()
    caminho = encontrar_caminho(g1, lab)
    print("Os nós encontrados foram: ")
    print(caminho)
    arestas_caminho = no_arestas(caminho, g1, lab)
    print("Tempo de execução para encontrar o caminho: ", time.time() - inicio)
    print("\nO caminho válido para o labirinto por meio das arestas é: ")
    print(arestas_caminho)
    
def imprime_lab(arquivo):
    with open(arquivo, "r") as file:
        lab = file.read()
    print(lab)


