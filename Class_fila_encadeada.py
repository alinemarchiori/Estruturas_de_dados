
class Noh:
    def __init__(self, dado):
        self.dado = dado
        self.proximo_elemento = None

class PilhaEncadeada:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def insere(self, dado):#insere no topo da pilha 

        if self.tamanho == 0:#verifica se está vazia
            self.inicio = Noh(dado)#insere o primeiro elemento
            self.fim = self.inicio
            self.tamanho += 1
        
        else:
            self.fim.proximo_elemento = Noh(dado) #insere no final
            self.tamanho += 1

        self.fim = Noh(dado)
    
    def remove(self):# remove do topo da pilha
        if self.inicio:
            auxiliar = self.inicio
            self.inicio = auxiliar.proximo_elemento

            auxiliar.proximo_elemento == None
            anterior.proximo_elemento = None
            self.tamanho -= 1

        else: return False

    def consulta(self): #retorna o valor do topo da pilha 
        if self.inicio:
            auxiliar = self.inicio
            while auxiliar.proximo_elemento: auxiliar = auxiliar.proximo_elemento
            return auxiliar.dado

        else: return "Vazia"

    def destruir(self): #remove todos os elementos
        while self.inicio.proximo_elemento: self.remove()
        self.tamanho,self.inicio = 0, None

    def compara_iguais(self, pilha2): # compara para ver se são iguais
        pilhaum = self.inicio
        pilhadois = pilha2.inicio
        
        if pilhaum.dado == pilhadois.dado:
            while pilhaum.proximo_elemento:
                pilhaum = pilhaum.proximo_elemento
                pilhadois = pilhadois.proximo_elemento
                if pilhaum.dado != pilhadois.dado: return False
            return True
        else: return False

    def mostra(self): # mostra elementos
        if self.tamanho == 0: print("lista vazia")
        objeto = self.inicio
        for i in range(self.tamanho):
            print(objeto.dado, end=" ")
            objeto = objeto.proximo_elemento
        print()
