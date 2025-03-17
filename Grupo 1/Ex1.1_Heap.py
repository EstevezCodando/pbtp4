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
        # Copiamos a lista para a estrutura de heap interna
        self.elementos = lista_inteiros[:]

        # Ajustamos a heap de trás para frente, chamando a função de "heapify"
        tamanho = len(self.elementos)
        for indice in range(tamanho // 2 - 1, -1, -1):
            self._heapify_para_baixo(indice, tamanho)

    def exibir_heap(self):
        """
        Exibe a heap em formato de lista.
        """
        print(self.elementos)

    def _heapify_para_baixo(self, indice_pai, tamanho):
        """
        Função interna que mantém a propriedade de min-heap deslocando 
        o valor para baixo quando necessário.
        """
        indice_esquerda = 2 * indice_pai + 1
        indice_direita = 2 * indice_pai + 2
        menor = indice_pai

        # Verifica se o filho da esquerda é menor que o pai
        if indice_esquerda < tamanho and self.elementos[indice_esquerda] < self.elementos[menor]:
            menor = indice_esquerda

        # Verifica se o filho da direita é menor que o atual 'menor'
        if indice_direita < tamanho and self.elementos[indice_direita] < self.elementos[menor]:
            menor = indice_direita

        # Se o menor não for o pai, faz a troca e continua o processo
        if menor != indice_pai:
            self.elementos[indice_pai], self.elementos[menor] = self.elementos[menor], self.elementos[indice_pai]
            self._heapify_para_baixo(menor, tamanho)



if __name__ == "__main__":
    lista_exemplo = [35, 33, 42, 10, 14, 19, 27, 44, 26, 31]

    heap_binaria = HeapBinaria()
    heap_binaria.construir_heap(lista_exemplo)

    print("Heap construída a partir da lista:")
    heap_binaria.exibir_heap()
