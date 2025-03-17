class HeapBinaria:
    """
    Classe que representa uma Heap Binária (min-heap).
    """

    def __init__(self):
        """
        Inicializa a heap como uma lista vazia.
        """
        self.elementos = []

    def construir_heap(self, lista_inteiros):
        """
        Recebe uma lista de inteiros e a transforma em uma min-heap binária.
        """
        self.elementos = lista_inteiros[:]
        tamanho = len(self.elementos)
        for indice in range(tamanho // 2 - 1, -1, -1):
            self._heapify_para_baixo(indice, tamanho)

    def exibir_heap(self):
        """
        Exibe a heap em formato de lista.
        """
        print(self.elementos)

    def inserir_elemento(self, novo_elemento):
        """
        Insere um novo elemento na heap e mantém a propriedade de min-heap.
        """
        self.elementos.append(novo_elemento)
        self._heapify_para_cima(len(self.elementos) - 1)

    def buscar_elemento(self, valor_buscado):
        """
        Busca um valor na heap.
        Retorna True se o valor estiver presente, False caso contrário.
        """
        if not self.elementos:
            return False

        # Implementação de BFS (ou DFS) com a otimização:
        # se o valor do nó atual for maior que 'valor_buscado', 
        # não precisamos visitar seus filhos.
        fila_indices = [0]  # Começamos pela raiz (índice 0)

        while fila_indices:
            indice_atual = fila_indices.pop(0)
            valor_atual = self.elementos[indice_atual]

            if valor_atual == valor_buscado:
                return True

            # Se o valor do nó atual for menor que o buscado,
            # existe a possibilidade de o valor estar nos filhos.
            # Se for maior, podemos descartar a subárvore.
            if valor_atual < valor_buscado:
                indice_esquerda = 2 * indice_atual + 1
                indice_direita = 2 * indice_atual + 2

                if indice_esquerda < len(self.elementos):
                    fila_indices.append(indice_esquerda)
                if indice_direita < len(self.elementos):
                    fila_indices.append(indice_direita)

        return False

    # Métodos internos da heap
    def _heapify_para_baixo(self, indice_pai, tamanho):
        """
        Ajusta a heap de cima para baixo, mantendo a propriedade de min-heap.
        """
        indice_esquerda = 2 * indice_pai + 1
        indice_direita = 2 * indice_pai + 2
        menor = indice_pai

        if indice_esquerda < tamanho and self.elementos[indice_esquerda] < self.elementos[menor]:
            menor = indice_esquerda
        if indice_direita < tamanho and self.elementos[indice_direita] < self.elementos[menor]:
            menor = indice_direita

        if menor != indice_pai:
            self.elementos[indice_pai], self.elementos[menor] = self.elementos[menor], self.elementos[indice_pai]
            self._heapify_para_baixo(menor, tamanho)

    def _heapify_para_cima(self, indice_atual):
        """
        Ajusta a heap de baixo para cima, mantendo a propriedade de min-heap.
        """
        while indice_atual > 0:
            indice_pai = (indice_atual - 1) // 2
            if self.elementos[indice_atual] < self.elementos[indice_pai]:
                self.elementos[indice_atual], self.elementos[indice_pai] = (
                    self.elementos[indice_pai],
                    self.elementos[indice_atual],
                )
                indice_atual = indice_pai
            else:
                break



if __name__ == "__main__":
    lista_exemplo = [35, 33, 42, 10, 14, 19, 27, 44, 26, 31]
    heap_binaria = HeapBinaria()

    # Construir heap a partir da lista
    heap_binaria.construir_heap(lista_exemplo)
    print("Heap construída a partir da lista inicial:")
    heap_binaria.exibir_heap()

    # Buscar um elemento que existe
    valor_procurado = 19
    encontrado = heap_binaria.buscar_elemento(valor_procurado)
    print(f"\nBuscando valor {valor_procurado} na heap: {encontrado}")

    # Buscar um elemento que não existe
    valor_procurado = 50
    encontrado = heap_binaria.buscar_elemento(valor_procurado)
    print(f"Buscando valor {valor_procurado} na heap: {encontrado}")
