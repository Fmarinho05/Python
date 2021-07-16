#def - Serve para definir funções onde terá uma sequencia de comandos, e quando você precisar dessas sequência em alguma parte do programa basta chama-la.

#Adicionando mais 1
def incremento(numero):
    numero = numero + 1
    return numero

print(incremento(5))

#Soma
def soma(primeiro, segundo):
    return primeiro + segundo

print(soma(5, 5))

#Subtração
def subtracao(linha1 , linha2):
    return linha1 - linha2

print(subtracao(50, 30))

#Multiplicação
def multiplicacao(primeiro, segundo):
    return primeiro * segundo

print(multiplicacao(10, 10))

#Divisão
def divisao(um, dois):
    return um / dois

print(divisao(20, 20))

#Potencia elevada
def expo(base, expoente):
    return base ** expoente

print(expo(5,1))
