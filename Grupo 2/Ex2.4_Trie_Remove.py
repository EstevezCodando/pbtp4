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
        no_atual = self.raiz
        for caractere in prefixo:
            if caractere not in no_atual.filhos:
                return []
            no_atual = no_atual.filhos[caractere]

        sugestoes = []

        def _dfs(no, caminho):
            if no.fim_palavra:
                sugestoes.append(prefixo + caminho)
            for char, filho in no.filhos.items():
                _dfs(filho, caminho + char)

        _dfs(no_atual, "")
        return sugestoes

    def remover_palavra(self, palavra):
        """
        Remove uma palavra específica do Trie, se existir.
        Remove nós que se tornem desnecessários (sem filhos e sem fim_palavra).
        Retorna True se a palavra foi removida; False caso contrário.
        """
        return self._remover_ajudante(self.raiz, palavra, 0)

    def _remover_ajudante(self, no_atual, palavra, indice):
        """
        Função recursiva auxiliar para remover a palavra.
        Retorna True se o nó filho pode ser removido do dicionário de 'filhos'.
        """
        # Caso base: se chegamos ao final da palavra
        if indice == len(palavra):
            # Se não for fim de palavra, significa que ela não existia
            if not no_atual.fim_palavra:
                return False
            # Marca que não é mais fim de palavra
            no_atual.fim_palavra = False
            # Se não há mais filhos, sinaliza que podemos remover este nó
            return len(no_atual.filhos) == 0

        caractere = palavra[indice]
        if caractere not in no_atual.filhos:
            return False  # A palavra não está no Trie

        # Chamada recursiva para o próximo caractere
        pode_remover_filho = self._remover_ajudante(no_atual.filhos[caractere], palavra, indice + 1)

        # Se podemos remover o nó filho (pois não é fim de outra palavra e não tem filhos)
        if pode_remover_filho:
            del no_atual.filhos[caractere]
            # Retorna True se não há mais filhos neste nó e não é fim de palavra
            return (len(no_atual.filhos) == 0) and (not no_atual.fim_palavra)

        return False

    def exibir_estrutura(self):
        """
        Exibe a estrutura do Trie para fins de depuração (opcional).
        """
        def _percorrer(no, prefixo):
            if no.fim_palavra:
                print(f"Palavra no Trie: {prefixo}")
            for char, filho in no.filhos.items():
                _percorrer(filho, prefixo + char)

        _percorrer(self.raiz, "")



if __name__ == "__main__":
    palavras_iniciais = ["casa", "casamento", "casulo", "cachorro"]
    trie = Trie()

    # Insere as palavras iniciais
    for palavra in palavras_iniciais:
        trie.inserir_palavra(palavra)

    print("Trie inicial:")
    trie.exibir_estrutura()

    # Verifica se "casa" está presente
    print("\nExiste 'casa'? ", trie.buscar_palavra("casa"))
    print("Autocomplete para 'cas': ", trie.listar_autocompletes("cas"))

    # Remove "casa"
    removido = trie.remover_palavra("casa")
    print(f"\nRemovendo 'casa': {'Sucesso' if removido else 'Falhou'}")

    # Verifica se "casa" ainda está presente
    print("Existe 'casa'? ", trie.buscar_palavra("casa"))
    print("Autocomplete para 'cas': ", trie.listar_autocompletes("cas"))

    print("\nTrie após remoção de 'casa':")
    trie.exibir_estrutura()
