import time

class Calculadora:
    def __init__(self):
        self.shift = 0
        self.primeiro = self.segundo = []
        self.matriz_soma = []
        self.tamanho = 0

    def soma(self, primeiro, segundo):

        x_str = str(primeiro)
        y_str = str(segundo)
        lista = []
        listax = []
        listay = []
        for i in x_str:
            listax.append(i)
        for i in y_str:
            listay.append(i)
        listax = list(map(int, listax))
        listay = list(map(int, listay))
        for i in range(10000): f = 0
        while(len(listax) != len(listay)):
            if(len(listax) < len(listay)):
                listax.insert(0,0)
            elif(len(listay) < len(listax)):
                listay.insert(0,0)
        listax = list(reversed(listax))
        listay = list(reversed(listay))
        a = 0
        for a in range(len(listax)):
            soma = listax[a] + listay[a]
            if soma <= 9:
                lista.append(soma)
            else:
                if (a+1 == len(listax)):
                    lista.append(soma)
                else:
                    listax[a+1] = listax[a+1] + 1
                    soma = soma - 10
                    lista.append(soma)
        lista = list(reversed(lista))
        resultado = int("".join(map(str, lista)))
        resultado = int(resultado)
        
        return resultado
        

    def multiplica(self, primeiro, segundo):

        self.primeiro, self.segundo = primeiro, segundo
        shift, soma = 0, 0

        for i in range(len(self.primeiro)-1,-1,-1):
            carry, numero = 0, ""

            for f in range(shift): numero += "0"

            for j in range(len(self.segundo)-1, -1, -1):
                result, carry = 0, int(carry)

                for k in range(int(self.primeiro[i])):
                    result = self.soma(result, int(self.segundo[j]))

                result = result + carry
                if result > 9:
                    r = str(result)
                    carry = r[0]
                    result = r[1]
                    numero = str(result) + numero
                else:
                    numero = str(result) + numero
                    carry = 0
                
                if 0 == j: numero = str(carry) + numero

            shift += 1
            soma = self.soma(soma, int(numero))

        return soma


def main():
    while True:
        operacao = Calculadora()
        escolha = int(input("1 - Multiplicacao;\n2 - Soma;\n3 - Sair.\n"))

        if escolha == 1:
            d1 = input("Digite o primeiro numero: ")
            d2 = input("Digite o segundo numero: ")
            inicio = time.time()
            resultado = operacao.multiplica(d1,d2)
            fim = time.time()
            print("O resultado eh:", resultado)
            print("O tempo: {:.10f}".format(fim-inicio))

        elif escolha == 2:
            d1 = input("Digite o primeiro numero: ")
            d2 = input("Digite o segundo numero: ")
            inicio = time.time()
            resultado = operacao.soma(int(d1), int(d2))
            fim = time.time()
            print("O resultado eh:", resultado)
            print("O tempo: {:.10f}".format(fim-inicio))
            
        elif escolha == 3:
            break

        else: print("opcao invalida")

main()