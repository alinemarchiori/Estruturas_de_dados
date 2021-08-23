class Tabela:
    def __init__(self, tamanhoMax):
        self.chave = [None] * (tamanhoMax + 1)
        self.valor = [None] * (tamanhoMax + 1)
        self.li = 1
        self.ls = tamanhoMax
        self.inicio = self.li - 1
        self.fim = self.ls + 1

    # funções solicitadas 

    def insereOrdenado(self):
        pass

    def buscaBInaria(self):
        pass

    # funções já prontas, feitas pelo professor:

    def __repr__(self):
        string = ""
        if not self.vazia():
            for i in range(self.inicio, self.fim + 1):
                string = string + str(self.chave[i]) + ": " + str(self.valor[i]) + "/n"
            return string + "/n"

    def vazia(self):
        return self.inicio < self.li or self.fim > self.ls

    def cheia(self):
        return self.inicio == self.li and self.fim == self.ls

    def tamanho(self):
        if not self.vazia():
            return self.fim - self.inicio + 1
        else:
            return 0

    def buscar(self, chave):
        if not self.vazia():
            for i in range(self.inicio, self.fim + 1):
                if self.chave[i] == chave:
                    return i
        return 0

    def inserir(self, chave, valor):
        posicao = self.buscar(chave)
        if posicao > 0:
            self.valor[posicao] = valor
        elif not self.cheia():
            if self.vazia():
                self.inicio = self.li
                self.fim = self.li
            else:
                self.fim += 1
            self.chave[self.fim] = valor
            self.valor[self.fim] = valor

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

    def destruir(self):
        self.inicio = self.li - 1
        self.fim = self.ls + 1

