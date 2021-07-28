class Calculadora:
    def __init__(self):
        pass

    def soma(self):
        pass

    def multiplica(self):
        pass


def main():
    operacao = Calculadora()
    while True:
        escolha = int(input("1 - Meltiplicacao;\n2 - Soma;\n3 - Sair."))
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