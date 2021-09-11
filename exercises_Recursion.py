from functools import reduce

'''
                                1) Implemente de maneira iterativa e recursiva a operação soma_elementos(). 
                                Esse método deve receber como parâmetro uma lista ou vetor contendo números 
                                e retornar a soma dos elementos desta lista. Por exemplo, se v = [1, 2, 3, 10], 
                                soma_elementos(v) deve retornar 16.
'''
def soma_elementos_recursivo(vetor):
    if len(vetor) == 1:
        return vetor[0]
    else:
        return soma_elementos_recursivo(vetor[1:]) + vetor[0]

def soma_elementos_iterativo(vetor):
    return int(reduce(lambda x,y: x+y, v))
    
v = [1, 2, 3, 4, 5]
print(soma_elementos_iterativo(v))
print(soma_elementos_recursivo(v))

'''
                                2) Implemente de maneira iterativa e recursiva um método que retorne o fatorial
                                de um número natural passado como argumento.
'''
def fatorial_recursivo(numero):
    if numero == 1 or numero == 0:
        return 1
    else:
        return fatorial_recursivo(numero-1)*numero

def fatorial_iterativo(numero):
    soma = numero
    for i in range(numero, 1, -1):
        soma = soma * (i - 1)
    return soma

print(fatorial_recursivo(40))
print(fatorial_iterativo(40))

'''
                                #3) Implemente de maneira iterativa e recursiva o cálculo de Fibonacci. 
                                # Consulte a aula para verificar um exemplo.
'''
def fib_recursivo(numero):
    if numero == 0 or numero == 1:
        return numero
    else:
        return fib_recursivo(numero-1)+fib_recursivo(numero-2)

def fib_iterativo(numero):
    if numero == 1 or numero == 0:
        return numero
    else:
        anterior, resultado = 0, 1
        for i in range(numero-1):
            aux = resultado
            resultado = resultado + anterior
            anterior = aux
        return resultado
a=9
print(fib_recursivo(a))
print(fib_iterativo(a))

'''
                                4) Implemente de maneira recursiva o método soma_digitos(). Este método recebe 
                                como parâmetro um número natural e retorna a soma dos dígitos. Por exemplo, 
                                soma_digitios(14) deve retornar 5.
'''
def soma_digitos(numero):  
    if numero < 10:
        return numero
    else:   
        return soma_digitos(numero//10)+(numero%10)

print(soma_digitos(23232323))