# PBTP4 - Estruturas de Dados

Este repositório reúne implementações de 5 grupos de exercícios, cobrindo:
1. **Heap Binária** (leitura, busca, inserção e remoção),
2. **Trie** (inserção, busca, autocomplete e remoção de palavras),
3. **Buscas em Grafos** (DFS, BFS e busca de caminhos).

Cada exercício possui um arquivo correspondente, com funções e exemplos de uso.

---

## 📂 Estrutura do Repositório

### **Grupo 1: Heap Binária**

1. [Ex1.1_Heap.py](Ex1.1_Heap.py)  
   - **Criação e leitura de Heap**  
   - Recebe uma lista de inteiros e a transforma em uma heap binária (min-heap ou max-heap).  
   - Apresenta a estrutura da heap em formato de lista.

2. [Ex1.2_Heap_Inserir.py](Ex1.2_Heap_Inserir.py)  
   - **Inserção de elemento na Heap**  
   - Dada uma heap existente, insere um novo elemento mantendo a propriedade de heap.  
   - Mostra o estado da heap antes e depois da inserção.

3. [Ex1.3_Heap_Busca.py](Ex1.3_Heap_Busca.py)  
   - **Busca de elemento na Heap**  
   - Verifica se um valor específico existe na heap, retornando `True` ou `False`.  
   - Percorre a heap de forma eficiente.

4. [Ex1.4_Heap_Remove.py](Ex1.4_Heap_Remove.py)  
   - **Remoção da raiz (menor ou maior, dependendo do tipo de heap)**  
   - Remove o elemento raiz (menor em min-heap ou maior em max-heap) e reestrutura a heap.  
   - Mostra o estado da heap antes e depois da remoção.

---

### **Grupo 2: Autocomplete com Trie**

1. [Grupo 1/Ex2.1_Trie.py](Ex2.1_Trie.py)  
   - **Criação de Trie e inserção de palavras**  
   - Classe `Trie` que insere palavras caractere a caractere.  
   - Inclui a inserção manual de uma lista de palavras.

2. [Ex2.2_Trie_Busca.py](Ex2.2_Trie_Busca.py)  
   - **Busca simples em Trie**  
   - Verifica se uma palavra está presente no Trie.  
   - Retorna `True` se a palavra for encontrada, caso contrário `False`.

3. [Ex2.3_Trie_Autocomplete.py](Ex2.3_Trie_Autocomplete.py)  
   - **Autocomplete básico**  
   - Dado um prefixo, retorna todas as palavras que começam com esse prefixo.

4. [Ex2.4_Trie_Remove.py](Ex2.4_Trie_Remove.py)  
   - **Remoção de palavra no Trie**  
   - Remove uma palavra específica, ajustando os nós necessários.  
   - Mantém as demais palavras intactas.

---

### **Grupo 3: Busca em Grafos (DFS e BFS)**

1. [Ex3.1_Grafo_ListAdj.py](Ex3.1_Grafo_ListAdj.py)  
   - **Representação de grafo em lista de adjacência**  
   - Constrói um grafo (orientado ou não) a partir de uma lista de arestas.

2. [Ex3.2_Grafo_DFS.py](Ex3.2_Grafo_DFS.py)  
   - **Depth-First Search (DFS)**  
   - Recebe um nó inicial e retorna a ordem de visita dos nós via DFS.

3. [Ex3.3_Grafo_BFS.py](Ex3.3_Grafo_BFS.py)  
   - **Breadth-First Search (BFS)**  
   - Recebe um nó inicial e retorna a ordem de visita dos nós via BFS.

4. [Ex3.4_Grafo_Caminho.py](Ex3.4_Grafo_Caminho.py)  
   - **Busca de caminho entre dois nós**  
   - Utiliza DFS ou BFS para verificar (e retornar) um caminho entre dois nós, se existir.

---


