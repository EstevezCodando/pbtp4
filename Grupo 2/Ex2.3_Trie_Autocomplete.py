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

    def buscar_palavra(self, palavra):
        """
        Verifica se uma palavra está presente no Trie.
        Retorna True se encontrada; caso contrário, False.
        """
        no_atual = self.raiz
        for caractere in palavra:
            if caractere not in no_atual.filhos:
                return False
            no_atual = no_atual.filhos[caractere]
        return no_atual.fim_palavra

    def listar_autocompletes(self, prefixo):
        """
        Retorna todas as palavras do Trie que começam com o prefixo fornecido.
        """
        # 1. Localizar o nó onde termina o prefixo
        no_atual = self.raiz
        for caractere in prefixo:
            if caractere not in no_atual.filhos:
                return []  # Se algum caractere não existir, não há sugestões
            no_atual = no_atual.filhos[caractere]

        # 2. A partir desse nó, coletar todas as palavras (DFS ou BFS)
        sugestoes = []

        def _dfs(no, caminho):
            if no.fim_palavra:
                # Construímos a palavra completa concatenando o prefixo + caminho
                sugestoes.append(prefixo + caminho)
            for char, filho in no.filhos.items():
                _dfs(filho, caminho + char)

        _dfs(no_atual, "")
        return sugestoes

    def exibir_estrutura(self):
        """
        Exibe a estrutura do Trie para fins de depuração (opcional).
        Mostra todas as palavras armazenadas.
        """
        def _percorrer(no, prefixo):
            if no.fim_palavra:
                print(f"Palavra no Trie: {prefixo}")
            for char, filho in no.filhos.items():
                _percorrer(filho, prefixo + char)
        _percorrer(self.raiz, "")



if __name__ == "__main__":
    lista_palavras = ["casa", "casamento", "carro", "carteira", "mapa", "mar", "maré"]
    trie = Trie()

    # Inserindo manualmente cada palavra
    for palavra in lista_palavras:
        trie.inserir_palavra(palavra)

    # Exibindo estrutura completa (opcional, para verificação)
    print("Estrutura do Trie (todas as palavras inseridas):")
    trie.exibir_estrutura()

    # Testando autocomplete
    prefixos_para_teste = ["cas", "car", "ma", "mari"]
    for prefixo in prefixos_para_teste:
        resultados = trie.listar_autocompletes(prefixo)
        print(f"\nSugestões para o prefixo '{prefixo}': {resultados}")
