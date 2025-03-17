class NoTrie:
    """
    Classe que representa um nó no Trie.
    """
    def __init__(self):
        self.filhos = {}
        self.fim_palavra = False


class Trie:
    """
    Classe que representa a estrutura Trie.
    """

    def __init__(self):
        self.raiz = NoTrie()

    def inserir_palavra(self, palavra):
        """
        Insere uma palavra no Trie, caractere a caractere.
        """
        no_atual = self.raiz
        for caractere in palavra:
            if caractere not in no_atual.filhos:
                no_atual.filhos[caractere] = NoTrie()
            no_atual = no_atual.filhos[caractere]
        no_atual.fim_palavra = True

    def exibir_estrutura(self):
        """
        Exibe a estrutura do Trie para fins de depuração.
        """
        def _percorrer(no, prefixo):
            if no.fim_palavra:
                print(f"Palavra no Trie: {prefixo}")
            for char, filho in no.filhos.items():
                _percorrer(filho, prefixo + char)

        _percorrer(self.raiz, "")

    def buscar_palavra(self, palavra):
        """
        Verifica se uma palavra está presente no Trie.
        Retorna True se encontrada; caso contrário, False.
        """
        no_atual = self.raiz
        for caractere in palavra:
            if caractere not in no_atual.filhos:
                return False  # Se o caractere não existe, a palavra não foi inserida
            no_atual = no_atual.filhos[caractere]

        # Verifica se o nó final corresponde realmente a uma palavra completa
        return no_atual.fim_palavra



if __name__ == "__main__":
    lista_palavras = ["casa", "casamento", "carro", "carteira", "mapa", "mar"]
    trie = Trie()

    # Inserindo palavras manualmente
    for palavra in lista_palavras:
        trie.inserir_palavra(palavra)

    # Exibindo o Trie
    print("Estrutura do Trie após inserir as palavras:")
    trie.exibir_estrutura()

    # Testando a busca de palavras
    palavras_para_buscar = ["casa", "carteira", "maria", "mar", "map"]
    for p in palavras_para_buscar:
        encontrado = trie.buscar_palavra(p)
        print(f"Palavra '{p}' encontrada? {encontrado}")
