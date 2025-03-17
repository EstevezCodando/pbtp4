from collections import deque

def encontrar_caminho_bfs(grafo, origem, destino):
    """
    Retorna uma lista de nós representando um caminho entre 'origem' e 'destino'
    usando BFS. Se não houver caminho, retorna None.
    """
    # Se origem ou destino não existem no grafo, encerra
    if origem not in grafo or destino not in grafo:
        return None

    visitados = set()
    fila = deque([origem])
    
    # Dicionário para rastrear o "pai" de cada nó (para reconstruir o caminho)
    pai = {origem: None}

    while fila:
        no_atual = fila.popleft()

        # Se encontramos o destino, podemos reconstruir o caminho
        if no_atual == destino:
            return reconstruir_caminho(pai, origem, destino)

        for vizinho in grafo[no_atual]:
            if vizinho not in visitados:
                visitados.add(vizinho)
                pai[vizinho] = no_atual  # O pai do vizinho passa a ser o nó atual
                fila.append(vizinho)

    # Se terminarmos o laço sem encontrar o destino, não há caminho
    return None

def reconstruir_caminho(pai, origem, destino):
    """
    Reconstrói o caminho a partir do dicionário 'pai', 
    começando no destino e subindo até a origem.
    """
    caminho = []
    no_atual = destino
    while no_atual is not None:
        caminho.append(no_atual)
        no_atual = pai[no_atual]  # Avança para o pai do nó atual
    caminho.reverse()  # Inverte para ficar do origem -> destino
    return caminho


if __name__ == "__main__":
    # Grafo não-orientado representado por lista de adjacência
    # A-B, A-C, B-D, C-D, D-E
    grafo_exemplo = {
        "A": ["B", "C"],
        "B": ["A", "D"],
        "C": ["A", "D"],
        "D": ["B", "C", "E"],
        "E": ["D"]
    }

    origem = "A"
    destino = "E"

    caminho_encontrado = encontrar_caminho_bfs(grafo_exemplo, origem, destino)
    if caminho_encontrado:
        print(f"Caminho entre {origem} e {destino} encontrado: {caminho_encontrado}")
    else:
        print(f"Não existe caminho entre {origem} e {destino} neste grafo.")
