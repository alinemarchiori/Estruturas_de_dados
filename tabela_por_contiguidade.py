class Tabela:
    def __init__(self, tamanhoMax):
        self.chave = [None] * (tamanhoMax + 1)
        self.valor = [None] * (tamanhoMax + 1)
        self.li = 1
        self.ls = tamanhoMax
        self.inicio = self.li - 1
        self.fim = self.inicio
        self.quantidade_elementos = 0

    # funções solicitadas 

    def insereOrdenado(self, chave, valor):
        posicao = self.buscar(chave)
        
        if posicao > 0:
            self.chave[posicao] = chave
            self.valor[posicao] = valor

        elif not self.cheia():
            if self.vazia():
                self.inicio = self.li
                self.fim = self.li
                self.chave[self.fim] = chave
                self.valor[self.fim] = valor
            else:
                if self.chave[self.inicio] > chave:
                    for i in range(self.fim+1, self.inicio, -1):
                        self.chave[i] = self.chave[i-1]
                        self.valor[i] = self.valor[i-1]
                    self.chave[self.inicio] = chave
                    self.valor[self.inicio] = valor
                elif self.chave[self.fim] < chave:
                    self.chave[self.fim+1] = chave
                    self.valor[self.fim+1] = valor
                else:
                    for j in range(self.inicio+1, self.fim+1):
                        if self.chave[j] > chave:
                            for i in range(self.fim+2, j, -1):
                                self.chave[i] = self.chave[i-1]
                                self.valor[i] = self.valor[i-1]
                            self.chave[j] = chave
                            self.valor[j] = valor
                            break
                self.fim += 1
            self.quantidade_elementos += 1

    def buscar(self, chave):
        #return self.buscaLinear(chave)
        return self.buscaBinaria(chave)

    #função de busca binária
    def buscaBinaria(self, chave):
        inicio = self.inicio
        fim = self.fim
        meio = 0
        if self.vazia():
            return self.inicio
        while fim >= inicio:
            meio = ((fim + inicio) // 2)
            if self.chave[meio] == chave:
                return meio
            if self.chave[meio] > chave:
                fim = meio-1
            if self.chave[meio] < chave:
                inicio = meio+1
        return 0

    # funções já prontas, feitas pelo professor:

    def __repr__(self):
        string = ""
        if not self.vazia():
            for i in range(self.inicio, self.fim+1):
                string = string + str(self.chave[i]) + ": " + str(self.valor[i]) + ","
            return string + "/n"

    def vazia(self):
        if self.quantidade_elementos > 0:
            return False
        return True

    def cheia(self):
        return self.inicio == self.li and self.fim == self.ls

    def tamanho(self):
        return quantidade_elementos

    def buscaLinear(self, chave):
        if not self.vazia():
            for i in range(self.inicio, self.fim + 1):
                if self.chave[i] == chave:
                    return i
        return 0

    def inserir(self, chave, valor):
        posicao = self.buscar(chave)
        if posicao > 0:
            self.chave[posicao] = chave
            self.valor[posicao] = valor
        elif not self.cheia():
            if self.vazia():
                self.inicio = self.li
                self.fim = self.li
            else:
                self.fim += 1
            self.chave[self.fim] = chave
            self.valor[self.fim] = valor
            self.quantidade_elementos += 1

    def consultar(self, chave):
        posicao = self.buscar(chave)
        if posicao > 0:
            return self.valor[posicao]

    def excluir(self, chave):
        posicao = self.buscar(chave)
        if posicao > 0:
            for i in range(posicao, self.fim):
                self.chave[i] = self.chave[i+1]
                self.valor[i] = self.valor[i+1]
            self.fim -= 1
        self.quantidade_elementos -= 1

    def destruir(self):
        self.quantidade_elementos == 0
        self.inicio = self.li - 1
        self.fim = self.ls + 1