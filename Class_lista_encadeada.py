class Noh:
    def __init__(self, dado):
        self.dado = dado
        self.proximo_elemento = None

class Lista:
    def __init__(self):
        self.inicio = None
        self.quantidade_itens = 0

    def insere(self, valor, posicao_item=-1):

        if self.inicio:
            auxiliar = self.inicio

            if posicao_item == -1: #insere no final
                while auxiliar.proximo_elemento:
                    auxiliar = auxiliar.proximo_elemento

                auxiliar.proximo_elemento = Noh(valor)
                self.quantidade_itens += 1

            elif posicao_item <= self.quantidade_itens and posicao_item > -1:#insere no meio
                contador = 0
                if posicao_item != 0: #insere no meio
                    while contador < posicao_item-1: 
                        auxiliar = auxiliar.proximo_elemento
                        contador += 1

                    posterior = auxiliar.proximo_elemento
                    auxiliar.proximo_elemento = Noh(valor)
                    anterior = auxiliar.proximo_elemento
                    anterior.proximo_elemento = posterior
                    self.quantidade_itens += 1

                else: #insere no início
                    aux = self.inicio
                    self.inicio = Noh(valor)
                    self.inicio.proximo_elemento = aux
                    self.quantidade_itens += 1

            else: print("Posicao invalida.")# fora do range

        else: # insere o primeiro elemento na lista
            self.inicio = Noh(valor)
            self.quantidade_itens += 1

    def remove(self, posicao_item):
        if self.inicio:
            auxiliar = self.inicio

            if posicao_item > 0 and posicao_item <= self.quantidade_itens:# remove do meio
                for i in range(0, posicao_item-1):
                    auxiliar = auxiliar.proximo_elemento
                remover = auxiliar.proximo_elemento
                auxiliar.proximo_elemento = remover.proximo_elemento
                self.quantidade_itens -= 1

            #remove do início
            elif posicao_item == 0: self.inicio = self.inicio.proximo_elemento; self.quantidade_itens -= 1
            else: print("posicao invalida")

        else: print("lista vazia")

    
    def posicao(self, valor):
        pass

    def valor(self, posicao_item):
        pass
    
    def destroi(self):
        pass

    def mostra(self): # mostra elementos
        objeto = self.inicio
        for i in range(self.quantidade_itens):
            print(objeto.dado, end=" ")
            objeto = objeto.proximo_elemento
        print()
    
    def vazia(self):
        if self.quantidade_itens <= 0:
            self.inicio = None

lista = Lista()
lista.insere(0, 0)
lista.insere(1)
lista.insere(2)
lista.insere(3)

lista.insere(5)
lista.insere(6)
lista.mostra()
lista.insere(4, 4)
lista.mostra()
lista.insere(0, 4)
lista.mostra()
lista.remove(0)
lista.mostra()
