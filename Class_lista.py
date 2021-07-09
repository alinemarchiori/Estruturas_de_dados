
class Produto:
    def __init__(self, valor=0, codigo=0, nome=""):
        self.valor = valor
        self.codigo = codigo
        self.nome = nome

    def getDados(self):
        return self.nome, self.valor, self.codigo

class Lista:
    def __init__(self, tamanho=20):

        self.tamanho = tamanho
        self.vetor = [Produto()] * self.tamanho
        self.valor_limite = self.tamanho - 1
        self.inicio_lista = self.tamanho//2
        self.inicio = None
        self.fim = None

    def consultar(self, posicao):
        
        if self.fim == None or self.inicio == None:
            return 'Lista vazia', 0, 0, False
            
        elif posicao > (self.fim - self.inicio + 1) or posicao < 1:
            print(posicao, (self.fim - self.inicio + 1), self.inicio)
            return 'Posicao invalida', 0, 0, False

        else:
            nome, valor, codigo = self.vetor[self.inicio + posicao - 1].getDados()
            return nome, valor, codigo, True

    def inserir_pos_i(self, novo, posicao, final):

        if self.inicio == None and self.fim == None:
            self.fim = self.inicio = self.tamanho//2
            self.vetor[self.fim] = novo
    
        elif posicao == (self.fim - self.inicio + 2) or final:#final da lista 
            self.fim += 1
            self.vetor[self.fim] = novo
        
        elif posicao == 1: #inicio da lista
            self.inicio -= 1
            self.vetor[self.inicio] = novo
    
        elif posicao > 1 and posicao < (self.fim - self.inicio + 2):# adiciona no meio (não funciona)
            tamanho_lista = self.fim - self.inicio + 1
            metade_lista = tamanho_lista//2
            print(metade_lista, tamanho_lista, posicao, (self.inicio+posicao), self.fim)
            if posicao >= metade_lista:
                for i in range(self.inicio+posicao,self.inicio+tamanho_lista,1):
                    print("entrei pra adicionar no meio   ", i)
                    auxiliar = self.vetor[i]
                    self.vetor[i] = novo
                    novo = auxiliar
                self.fim += 1
            elif posicao < metade_lista:
                for i in range(self.inicio+posicao,self.inicio+tamanho_lista,1):
                    print("entrei pra adicionar no meio   ", i)
                    auxiliar = self.vetor[i]
                    self.vetor[i] = novo
                    novo = auxiliar
                self.fim += 1
        '''
        elif posicao > 1 and posicao < (self.fim - self.inicio + 2):# adiciona no inicio da lista também
            tamanho_lista = self.fim - self.inicio + 1
            metade_lista = tamanho_lista//2
            print(metade_lista, tamanho_lista, posicao, (self.inicio+posicao))
            if posicao >= metade_lista:
                for i in range(self.inicio,self.inicio+tamanho_lista,1):
                    print("entrei pra adicionar no meio   ", i)
                    auxiliar = self.vetor[i]
                    self.vetor[i] = novo
                    novo = auxiliar
                self.fim += 1'''

        

    def remover_pos_i(self):
        pass

    def getPosicao(self):
        pass

    def limpar(self):
        pass

    def mostra(self, posicao):
        nome, valor, codigo, verifica = lista.consultar(posicao)
        print(verifica)
        if verifica:
            #print("Nome: {}\nValor: {} reais\nCodigo: {}".format(nome, valor, codigo))
            print(nome)
            print("todos os elementos: ", end='')
            for i in range(self.inicio, self.fim+1):
                print(self.vetor[i].nome, end=", ")
            print("/n")
        else: 
            print(nome)

#################################################

lista = Lista()
'''
novo = Produto(1.0, 1, "teste")
lista.inserir_pos_i(novo, 1)
novo = Produto(2.0, 2, "teste2")
lista.inserir_pos_i(novo, 2)
novo = Produto(3.0, 3, "teste3")
lista.inserir_pos_i(novo, 3)
novo = Produto(4.0, 4, "teste4")
lista.inserir_pos_i(novo, 4)'''

while True:
    #print("0 - Sair")
    print("1 - Inserir um elemento na lista")
    #print("2 - Remover um elemento da lista")
    print("3 - Consultar um elemento da lista")
    escolha = int(input())

    if escolha == 0:
        break
    elif escolha == 1:
        posicao = input("Digite a posição")
        valor, codigo, nome = input("informe o valor, codigo e nome").split()
        novo = Produto(float(valor), int(codigo), nome)
        if posicao == "":
            lista.inserir_pos_i(novo, int(posicao), True)
        else:
            lista.inserir_pos_i(novo, int(posicao), False)
    elif escolha == 2:
        pass

    elif escolha == 3:
        posicao = int(input("Digite a posicao: "))
        lista.mostra(posicao)


