
class Noh:
    def __init__(self, dado):
        self.dado = dado
        self.proximo_elemento = None

class FilaEncadeada:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

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

fila.mostra()

fila.insere(23)
fila.insere(22)
fila.insere(21)
fila.insere(20)
print(fila.consulta())
fila.remove()
print(fila.consulta())
fila.mostra()
print(fila.consulta())
