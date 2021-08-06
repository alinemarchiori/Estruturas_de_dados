#Aline dos Santos Marchiori - 132796

class Noh:
    def __init__(self):
        self.dado = dado
        self.proximo_elemento = None

class PilhaEncadeada:
    def __init__(self):
        self.inicio = None

    def insere(self, dado):
        pass
    
    def remove(self):
        pass

    def consulta(self):
        pass

class PilhaContiguidade:

    def __init__(self, tamanho=100):
        self.vetor = [None] * tamanho
        self.topo = None
        self.inicio = None
        self.tamanho = 0

    def insere(self, dado):
        if self.tamanho == 0:
            self.inicio = self.topo = 0

        self.vetor[self.topo] = dado
        self.tamanho += 1
        self.topo += 1

    def remove(self): 
        if self.topo == 1:
            self.topo = None
            self.tamanho = 0
        else: 
            self.topo -= 1
            self.tamanho -= 1
    
    def consulta(self):
        if self.tamanho != 0: return self.vetor[self.topo]
        else: return "Pilha vazia"

    def limpa(self): self.topo = self.inicio = None; self.tamanho = 0

    def mostraPilhaContiguidade(self):#AUTOEXPLICATIVA
        if self.topo == None or self.inicio == None:
            print("Pilha vazia")
        else:
            for i in range(self.inicio, self.topo,1):
                if i == self.inicio:
                    print("["+ str(self.vetor[i]), end="")
                else: print(",", self.vetor[i], end="")
            print("] ")

    ''' #TESTES PILHA POR CONTIGUIDADE
    pilha_contiguidade = PilhaContiguidade()

    pilha_contiguidade.insere(23)
    pilha_contiguidade.insere(3)
    pilha_contiguidade.insere(2)

    pilha_contiguidade.mostraPilhaContiguidade()

    pilha_contiguidade.remove()
    pilha_contiguidade.remove()

    pilha_contiguidade.mostraPilhaContiguidade()

    print(pilha_contiguidade.consulta())

    pilha_contiguidade.remove()

    print(pilha_contiguidade.consulta())

    pilha_contiguidade.mostraPilhaContiguidade()'''

#TESTES PILHA ENCADEADA

