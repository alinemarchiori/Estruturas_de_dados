############################################################################################

# FUNÇÕES DISPONÍVEIS
#---------------------------------------------insere elemento
#   lista.inserir_pos_i(ELEMENTO, POSIÇÃO) 
#---------------------------------------------remove elemento pela posição
#   lista.remover_pos_i(POSIÇÃO)
#---------------------------------------------mostra o elemento da posição indicada
#   lista.mostra(POSIÇÃO)
#---------------------------------------------mostra o elemento informando o atributo (codigo) do abjeto Produto
#   lista.getPosicao(CÓDIGO)
#---------------------------------------------mostra a lista toda
#   lista.mostraLista()
#---------------------------------------------apaga todos os elementos
#   lista.limpar()
#---------------------------------------------retorna o tamanho da lista
#   lista.dimensione()

############################################################################################



class Produto:
    def __init__(self, valor=0, codigo=0, nome=""):

        self.valor = valor
        self.codigo = codigo
        self.nome = nome

    def getDados(self):

        return self.nome, self.valor, self.codigo
    
    def getCodigo(self):

        return self.codigo

class Lista:
    def __init__(self, tamanho=100):

        self.tamanho = tamanho
        self.vetor = [Produto()] * self.tamanho
        self.valor_limite = self.tamanho - 1
        self.inicio_lista = self.tamanho//2
        self.inicio = None
        self.fim = None

    def consultar(self, posicao=-1): #FUNÇÃO INTERNA
        
        if self.fim == None or self.inicio == None: return 'Lista vazia', 0, 0, False
            
        elif posicao > (self.fim - self.inicio + 1) or posicao < 1: return 'Posicao invalida', 0, 0, False

        else:
            nome, valor, codigo = self.vetor[self.inicio + posicao - 1].getDados()
            return nome, valor, codigo, True

    def inserir_pos_i(self, novo, posicao):#INSERIR

        if self.inicio == None and self.fim == None: #adiciona quando a lista está vazia

            if posicao < -1 or posicao > self.valor_limite:

                print("Posicao invalida, seu elemento foi inserido no inicio da lista!")

            self.fim = self.inicio = self.tamanho//2
            self.vetor[self.fim] = novo
    
        elif posicao == (self.fim - self.inicio + 2) or posicao == -1:#final da lista 
            
            self.fim += 1
            self.vetor[self.fim] = novo
        
        elif posicao == 1: #inicio da lista
            
            self.inicio -= 1
            self.fim += 1 ############ não sei se precisa (teoricamente aumenta um no fim)
            self.vetor[self.inicio] = novo
    
        elif posicao > 1 and posicao < (self.fim - self.inicio + 2):# adiciona no meio (funciona)
            
            lista.tam()

            if posicao >= self.metade_lista:# adiciona empurrando os elementos da metade para a direita

                for i in range(self.inicio+posicao-1, self.inicio+self.tamanho_lista+1, 1):
                   
                    auxiliar = self.vetor[i]
                    self.vetor[i] = novo
                    novo = auxiliar

                self.fim += 1

            elif posicao < self.metade_lista:# adiciona empurrando os elementos da metade para a esquerda
                
                cont = posicao - 1

                while cont >= 0:

                    auxiliar = self.vetor[self.inicio + cont - 1]
                    self.vetor[self.inicio+cont-1] = novo
                    novo = auxiliar
                    cont -= 1

                self.inicio -= 1

        else: print("Posicao invalida!")

    def tam(self):#FUNÇÃO INTERNA

        self.tamanho_lista = self.fim - self.inicio + 1
        self.metade_lista = self.tamanho_lista//2

    def dimensione(self):#TAMANHO

        if self.fim == None: return 0; 
        else: return(self.fim - self.inicio + 1)
        
    def remover_pos_i(self, posicao):#REMOVE
        
        nome, valor, codigo, verifica = lista.consultar(posicao)
        vazia = False
        if lista.dimensione() == 1: vazia = True #serve para quando tem um só elemente e ele é removido, aí eu zero as variáveis de início e fim

        if verifica:

            lista.tam()

            if posicao >= self.metade_lista: # remove empurrando os elementos para a esquerda 

                cont = - 1

                for i in range(self.inicio + posicao - 1, self.fim, 1):

                    self.vetor[self.inicio + posicao + cont] = self.vetor[self.inicio + posicao + cont+1]
                    cont += 1

                self.fim -= 1

            elif posicao < self.metade_lista: # remove empurrando os elementos para a direita
        
                for i in range(0, posicao, 1):

                    self.vetor[self.inicio + posicao-1] = self.vetor[self.inicio + posicao - 2]
                    posicao -= 1
                
                self.inicio += 1

            else: print(nome)
            if vazia == True: lista.limpar()

    def getPosicao(self, codigo):#POSIÇÃO

        if self.fim == None or self.inicio == None:

            print("Lista vazia")
            return None

        else:

            posicao = 1
            verifica = False

            for i in range(0, self.fim - self.inicio + 1, 1):
                
                if self.vetor[self.inicio+i].getCodigo() == codigo:

                    return posicao

                else: posicao += 1

            print("Elemento nao encontrado")
            return None

    def limpar(self):#AUTOEXPLICATIVA

        self.inicio = self.fim = None

    def mostra(self, posicao):#MOSTRA ELEMENTO

        nome, valor, codigo, verifica = lista.consultar(posicao)
       
        if verifica:

            print("Nome: {}\nValor: {} reais\nCodigo: {}".format(nome, valor, codigo))

        else: 

            print(nome)

    def mostraLista(self):#AUTOEXPLICATIVA

        if self.fim == None or self.inicio == None:

            print("Lista vazia")

        else:

            for i in range(self.inicio, self.fim+1,1):

                if i == self.inicio:
                    print("["+ str(self.vetor[i].nome), end="")

                else: print(",", self.vetor[i].nome, end="")

            print("] ")


###############################################################################################################################

lista = Lista()

while True:

    print("0 - Sair")
    print("1 - Inserir um elemento na lista:")
    print("2 - Remover um elemento da lista")
    print("3 - Consultar um elemento da lista pela posicao:")
    print("4 - Encontrar um produto pelo codigo:")
    print("5 - Ver lista de produtos:")
    print("6 - Apagar todos os elementos:")
    print("7 - Ver o tamanho da lista")
    escolha = int(input())

    ######### ENCERRAR
    if escolha == 0:

        break

    ######### INSERIR
    elif escolha == 1:

        posicao = input("Digite a posição se quiser: ")
        valor, codigo, nome = input("informe o valor, codigo e nome: ").split()
        novo = Produto(float(valor), int(codigo), nome)

        if posicao == "" or posicao == -1:

            posicao=-1
            lista.inserir_pos_i(novo, posicao)

        else:
            lista.inserir_pos_i(novo, int(posicao))
    
    ######### APAGAR UM ELEMENTO PELA POSIÇÃO
    elif escolha == 2:

        posicao = int(input("Digite a posicao: "))
        lista.remover_pos_i(posicao)

    ######### MOSTRAR
    elif escolha == 3:

        posicao = int(input("Digite a posicao: "))
        lista.mostra(posicao)

    ######### MOSTRAR A POSIÇÃO DE ACORDO COM O CÓDIGO
    elif escolha == 4:

        codigo = int(input("Informe o codigo do produto: "))
        posicao = lista.getPosicao(codigo)

        if posicao != None:

            lista.mostra(posicao)
            print("O produto de codigo {} está na posicao {} da lista.".format(codigo, posicao))

    ######### MOSTRAR TODA A LISTA
    elif escolha == 5:
        lista.mostraLista()

    ######### APAGAR TODOS OS ELEMENTOS
    elif escolha == 6:
        lista.limpar()

    ######### MOSTRAR O TAMANHO DA LISTA
    elif escolha == 7:
        print(lista.dimensione())

    else: print("Posicao invalida!")