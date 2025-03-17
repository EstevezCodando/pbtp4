def dfs(grafo, no_inicial):
    """
    Realiza a busca em profundidade (DFS) em um grafo representado por lista de adjacência.
    
    :param grafo: Dicionário que mapeia cada nó a uma lista de nós adjacentes.
    :param no_inicial: Nó a partir do qual a busca em profundidade será iniciada.
    :return: Lista com a ordem de visita dos nós.
    """
    visitados = set()
    ordem_visita = []
    pilha = [no_inicial]  # Usamos uma pilha para simular a recursão da DFS

    while pilha:
        no_atual = pilha.pop()
        if no_atual not in visitados:
            visitados.add(no_atual)
            ordem_visita.append(no_atual)

            # Adicionamos os vizinhos na pilha.
            # Se quisermos manter a ordem de visita igual à ordem na lista de adjacência,
            # podemos iterar diretamente (sem 'reversed').
            for vizinho in reversed(grafo.get(no_atual, [])):
                if vizinho not in visitados:
                    pilha.append(vizinho)

    return ordem_visita


if __name__ == "__main__":
    # Exemplo simples de um grafo não-orientado em lista de adjacência
    # Note que, se fosse orientado, só adicionaríamos o nó destino na lista do nó origem.
    grafo_exemplo = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"],
        "E": ["B", "F"],
        "F": ["C", "E"]
    }

    no_inicial = "A"
    resultado_dfs = dfs(grafo_exemplo, no_inicial)
    print(f"Ordem de visita iniciando em '{no_inicial}': {resultado_dfs}")
