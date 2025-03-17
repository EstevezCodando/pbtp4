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
        
        Utiliza BFS/DFS com otimização:
        Se o valor do nó atual for maior que 'valor_buscado', descarta-se a subárvore.
        """
        if not self.elementos:
            return False

        fila_indices = [0]  # Começamos pela raiz (índice 0)

        while fila_indices:
            indice_atual = fila_indices.pop(0)
            valor_atual = self.elementos[indice_atual]

            if valor_atual == valor_buscado:
                return True

            if valor_atual < valor_buscado:
                indice_esquerda = 2 * indice_atual + 1
                indice_direita = 2 * indice_atual + 2

                if indice_esquerda < len(self.elementos):
                    fila_indices.append(indice_esquerda)
                if indice_direita < len(self.elementos):
                    fila_indices.append(indice_direita)

        return False

    def remover_raiz(self):
        """
        Remove o menor elemento (raiz da min-heap) e reestrutura a heap.
        Retorna o valor removido ou None se a heap estiver vazia.
        """
        if not self.elementos:
            return None  # Heap vazia

        # Se houver apenas um elemento, este é a raiz e será removido
        if len(self.elementos) == 1:
            return self.elementos.pop()

        # 1. Salvar o valor da raiz
        valor_removido = self.elementos[0]

        # 2. Mover o último elemento para a raiz
        self.elementos[0] = self.elementos.pop()

        # 3. "Heapify" de cima para baixo para corrigir a propriedade de min-heap
        self._heapify_para_baixo(0, len(self.elementos))

        return valor_removido

    # Métodos privados para manutenção do heap
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
    # Exemplo de lista dada
    lista_exemplo = [5, 2, 3, 7, 1]

    # Passo 1: Construir a min-heap
    heap_binaria = HeapBinaria()
    heap_binaria.construir_heap(lista_exemplo)
    print("Heap construída a partir da lista inicial:")
    heap_binaria.exibir_heap()

    # Passo 2: Inserir um valor (0)
    novo_valor = 0
    print(f"\nInserindo o valor {novo_valor} na heap...")
    heap_binaria.inserir_elemento(novo_valor)
    print("Heap após inserção:")
    heap_binaria.exibir_heap()

    # Passo 3: Buscar um elemento (7)
    valor_buscado = 7
    encontrado = heap_binaria.buscar_elemento(valor_buscado)
    print(f"\nBuscando o valor {valor_buscado} na heap: {encontrado}")

    # Passo 4: Remover o menor elemento (raiz)
    print("\nRemovendo o menor elemento (raiz) da heap...")
    print("Heap antes da remoção:")
    heap_binaria.exibir_heap()

    raiz_removida = heap_binaria.remover_raiz()
    print(f"Valor removido: {raiz_removida}")

    print("Heap após a remoção:")
    heap_binaria.exibir_heap()
