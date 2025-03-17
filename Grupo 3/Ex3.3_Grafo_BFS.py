from collections import deque

def bfs(grafo, no_inicial):
    """
    Realiza a busca em largura (BFS) em um grafo representado por lista de adjacência.
    
    :param grafo: Dicionário que mapeia cada nó a uma lista de nós adjacentes.
    :param no_inicial: Nó a partir do qual a busca em largura será iniciada.
    :return: Lista com a ordem de visita dos nós.
    """
    visitados = set()
    ordem_visita = []
    fila = deque([no_inicial])  # Usamos uma fila para a BFS

    while fila:
        no_atual = fila.popleft()

        if no_atual not in visitados:
            visitados.add(no_atual)
            ordem_visita.append(no_atual)

            # Adiciona na fila todos os vizinhos não visitados
            for vizinho in grafo.get(no_atual, []):
                if vizinho not in visitados:
                    fila.append(vizinho)

    return ordem_visita


if __name__ == "__main__":
    # Exemplo simples de um grafo não-orientado em lista de adjacência
    grafo_exemplo = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"],
        "E": ["B", "F"],
        "F": ["C", "E"]
    }

    no_inicial = "A"
    resultado_bfs = bfs(grafo_exemplo, no_inicial)
    print(f"Ordem de visita iniciando em '{no_inicial}': {resultado_bfs}")
