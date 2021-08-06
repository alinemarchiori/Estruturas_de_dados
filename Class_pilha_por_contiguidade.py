
class PilhaContiguidade:

    def __init__(self, tamanho=100):
        self.vetor = [None] * tamanho
        self.topo = None
        self.inicio = None
        self.tamanho = 0

    def insere(self, dado): #insere no topo
        if self.tamanho == 0: #verifica se está vazia 
            self.inicio = self.topo = 0

        self.vetor[self.topo] = dado
        self.tamanho += 1
        self.topo += 1

    def remove(self): #remove do topo da pilha
        if self.topo == 1:
            self.topo = None
            self.tamanho = 0
        else: 
            self.topo -= 1
            self.tamanho -= 1
    
    def consulta(self): #consulta o topo da pilha
        if self.tamanho != 0: return self.vetor[self.topo]
        else: return "Pilha vazia"

    def limpa(self): self.topo = self.inicio = None; self.tamanho = 0 #deixa a pilha vazia

    def mostraPilhaContiguidade(self): # mostra a pilha na tela, em formato de lista
        if self.topo == None or self.inicio == None:
            print("Pilha vazia")
        else:
            for i in range(self.inicio, self.topo,1):
                if i == self.inicio:
                    print("["+ str(self.vetor[i]), end="")
                else: print(",", self.vetor[i], end="")
            print("] ")
    
    def compara_iguais(self, pilha2):
        topo = self.topo
        for i in range(self.topo, self.inicio-1, -1):
            if pilha2.vetor[self.topo] != self.vetor[self.topo]: self.topo = topo; return False
            self.topo -= 1
        self.topo = topo
        return True
