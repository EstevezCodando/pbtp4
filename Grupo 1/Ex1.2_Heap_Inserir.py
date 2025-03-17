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
        Recebe uma lista de inteiros e transforma em uma min-heap binária.
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
        # Adiciona o elemento no final da lista
        self.elementos.append(novo_elemento)

        # Executa o heapify "para cima" a partir do último índice
        self._heapify_para_cima(len(self.elementos) - 1)

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

            # Se o elemento atual for menor que o pai, trocamos
            if self.elementos[indice_atual] < self.elementos[indice_pai]:
                self.elementos[indice_atual], self.elementos[indice_pai] = (
                    self.elementos[indice_pai],
                    self.elementos[indice_atual],
                )
                indice_atual = indice_pai
            else:
                # Se não for menor, a propriedade de min-heap está mantida
                break


if __name__ == "__main__":
    lista_exemplo = [35, 33, 42, 10, 14, 19, 27, 44, 26, 31]

    heap_binaria = HeapBinaria()
    heap_binaria.construir_heap(lista_exemplo)

    print("Heap construída a partir da lista inicial:")
    heap_binaria.exibir_heap()

    # Inserir um novo elemento
    novo_elemento = 8
    print(f"\nInserindo o elemento {novo_elemento} na heap...")
    print("Estado da heap antes da inserção:")
    heap_binaria.exibir_heap()

    heap_binaria.inserir_elemento(novo_elemento)

    print("\nEstado da heap depois da inserção:")
    heap_binaria.exibir_heap()
