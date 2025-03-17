def construir_grafo_lista_adjacencia(lista_arestas, orientado=False):
    """
    Constrói um grafo em forma de lista de adjacência a partir de uma lista de arestas.
    
    :param lista_arestas: Lista de tuplas (origem, destino), representando cada aresta.
    :param orientado: Se for True, o grafo será orientado; caso contrário, será não-orientado.
    :return: Dicionário (grafo) em forma de lista de adjacência.
    """
    grafo = {}

    for (origem, destino) in lista_arestas:
        # Se a origem não existe ainda no dicionário, inicializa com lista vazia
        if origem not in grafo:
            grafo[origem] = []
        # Adiciona o destino na lista de adjacência da origem
        grafo[origem].append(destino)

        # Se for não-orientado, adicionamos a origem na lista do destino
        if not orientado:
            if destino not in grafo:
                grafo[destino] = []
            grafo[destino].append(origem)

    return grafo



if __name__ == "__main__":
    # Lista de arestas. Exemplo: um grafo simples com 5 nós (A, B, C, D, E)
    # e algumas conexões.
    arestas_exemplo = [
        ("A", "B"),
        ("A", "C"),
        ("B", "C"),
        ("B", "D"),
        ("D", "E")
    ]

    # Construir um grafo não-orientado
    grafo_nao_orientado = construir_grafo_lista_adjacencia(arestas_exemplo, orientado=False)
    print("Grafo não-orientado (lista de adjacência):")
    for vertice, adjacentes in grafo_nao_orientado.items():
        print(f"{vertice}: {adjacentes}")

    # Construir um grafo orientado
    grafo_orientado = construir_grafo_lista_adjacencia(arestas_exemplo, orientado=True)
    print("\nGrafo orientado (lista de adjacência):")
    for vertice, adjacentes in grafo_orientado.items():
        print(f"{vertice}: {adjacentes}")
