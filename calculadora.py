class Calculadora:
    def __init__(self):
        self.shift = 0
        self.primeiro = self.segundo = []
        self.matriz_soma = None

    def soma(self, primeiro, segundo):
        return primeiro + segundo

    def multiplica(self, primeiro, segundo):
        self.matriz_soma = [0] * (len(primeiro) + len(primeiro))
        self.primeiro, self.segundo = primeiro, segundo
        carry, self.shift , resto = 0, 0, 0
        for i in range(len(primeiro)-1, 0, -1):
            multiplicador, carry = int(primeiro[i]), 0
            for i in range(len(segundo)-1, 0, -1):
                multiplicando, result = int(segundo[i]), 0
                for i in range(multiplicador):
                    result = self.soma(result,multiplicando)
                result = result + carry
                if result > 9:
                    result = list(str(result))
                    resto = int(result[1])
                    carry = int(result[0])
                else:
                    carry = 0

    def addMatrizSoma(self, n):
        pass

    def adicionaZeros(self, numero, tamanho):
        lista = [0] * tamanho
        numero = lista + numero

    def normalizaTamanho(self):
        if len(self.primeiro) > len(self.segundo):
            self.segundo = self.adicionaZeros(self.segundo, len(self.primeiro)-len(self.segundo))

                    



def main():
    operacao = Calculadora()
    while True:
        escolha = int(input("1 - Multiplicacao;\n2 - Soma;\n3 - Sair."))
        if escolha == 1:
            d1 = input("Digite o primeiro numero: ")
            d2 = input("Digite o segundo numero: ")
            operacao.multiplica(list(d1), list(d2))
        elif escolha == 2:
            d1 = input("Digite o primeiro numero: ")
            d2 = input("Digite o segundo numero: ")
            operacao.soma(list(d1), list(d2))
        elif escolha == 3:
            break
        else: print("opcao invalida")

main()