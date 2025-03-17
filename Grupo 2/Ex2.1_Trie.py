class NoTrie:
    """
    Classe que representa um nó no Trie.
    Armazena um dicionário de filhos e um indicador de fim de palavra.
    """
    def __init__(self):
        self.filhos = {}       # Dicionário (char -> NoTrie)
        self.fim_palavra = False


class Trie:
    """
    Classe que representa a estrutura Trie.
    """

    def __init__(self):
        """
        Inicializa o Trie com um nó raiz vazio.
        """
        self.raiz = NoTrie()

    def inserir_palavra(self, palavra):
        """
        Insere uma palavra no Trie, caracter por caracter.
        """
        no_atual = self.raiz

        for caractere in palavra:
            if caractere not in no_atual.filhos:
                no_atual.filhos[caractere] = NoTrie()
            no_atual = no_atual.filhos[caractere]

        # Marca que este nó corresponde ao fim de uma palavra completa
        no_atual.fim_palavra = True

    def exibir_estrutura(self):
        """
        Exibe a estrutura do Trie para fins de depuração (opcional).
        Percorre recursivamente cada caminho de caracteres.
        """

        def _percorrer(no, prefixo):
            if no.fim_palavra:
                print(f"Palavra no Trie: {prefixo}")
            for char, filho in no.filhos.items():
                _percorrer(filho, prefixo + char)

        _percorrer(self.raiz, "")


# -------------------------------------------
# EXEMPLO DE USO (teste):
# -------------------------------------------
if __name__ == "__main__":
    # Lista de palavras a serem inseridas no Trie
    lista_palavras = ["casa", "casamento", "carro", "carteira", "mapa", "mar"]

    trie = Trie()

    # Inserindo cada palavra manualmente
    for palavra in lista_palavras:
        trie.inserir_palavra(palavra)

    # Exibindo o que foi inserido no Trie (opcional, para verificação)
    print("Estrutura do Trie após inserir as palavras:")
    trie.exibir_estrutura()
