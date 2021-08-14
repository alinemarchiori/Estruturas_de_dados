from Class_pilha_encadeada import *


class Noh:
    def __init__(self, dado):
        self.dado = dado
        self.proximo_elemento = None

class FilaEncadeada:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def ordena(self):
        pilha1 = PilhaEncadeada()
        pilha2 = PilhaEncadeada()
        while self.tamanho > 0:
            if pilha1.tamanho == 0:
                pilha1.insere(self.inicio.dado)
                self.remove()

            elif self.inicio.dado >= pilha1.consulta():
            
                while self.inicio.dado > pilha1.consulta():
                    
                    pilha2.insere(pilha1.consulta())
                    pilha1.remove()
                    if pilha1.consulta() == None: break

                pilha1.insere(self.inicio.dado)

                while pilha2.consulta():
                    pilha1.insere(pilha2.consulta())
                    pilha2.remove()
                
                self.remove()

            elif self.inicio.dado < pilha1.consulta():
                pilha1.insere(self.inicio.dado)
                self.remove()

        while pilha1.consulta():
            self.insere(pilha1.consulta())
            pilha1.remove()

        pilha2.mostra()
        pilha1.mostra()

    def insere(self, dado):#insere no final da fila
        novo = Noh(dado)
        if self.tamanho == 0:#verifica se está vazia
            self.inicio = novo#insere o primeiro elemento
            self.fim = self.inicio
            self.tamanho += 1
        
        else:
            self.fim.proximo_elemento = novo #insere no final
            self.tamanho += 1

        self.fim = novo
    
    def remove(self):# remove do inicio da fila
        if self.inicio:
            auxiliar = self.inicio
            self.inicio = auxiliar.proximo_elemento
            self.tamanho -= 1

        else: return False

    def consulta(self): #retorna o valor do inicio da fila
        if self.inicio:
            return self.inicio.dado
            
        else: return None

    def destruir(self): #remove todos os elementos
        while self.inicio.proximo_elemento: self.remove()
        self.tamanho,self.inicio, self.fim = 0, None, None


    def mostra(self): # mostra elementos
        if self.tamanho == 0: print("fila vazia")
        objeto = self.inicio
        for i in range(self.tamanho):
            print(objeto.dado, end=" ")
            objeto = objeto.proximo_elemento
        print()

fila = FilaEncadeada()
print("----------")
fila.mostra()
print("----------")
fila.insere(2)
fila.insere(1)
fila.insere(4)
fila.insere(6)
fila.ordena()

fila.mostra()

fila.remove()

fila.mostra()
