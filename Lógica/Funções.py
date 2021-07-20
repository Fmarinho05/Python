#def - Serve para criar funções onde terá uma sequencia de comandos, e quando você precisar dessas sequência em alguma parte do programa basta chama-la.

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

#Divisão - Realiza a divisão e dá o resultado baseado na razão da operação, ou seja, será retornado um valor com casas decimais.
def divisao(um, dois):
    return um / dois

print(divisao(20, 20))

#MOD - É um operador aritmético que é responsável por retornar o resto de uma divisão.
def resto(a, b):
    return a % b

print(resto(14,4))

#DIV - Realiza a divisão e dá o resultado baseado no quociente.
def quociente(a, b):
    return a // b

print(quociente(14, 4))

#Potencia elevada
# def expo(base, expoente):
#     return base ** expoente

# print(expo(5,10))

#Função com entradas de teclados.
def expo(base, expoente):
    if type(base) == type("") or type(expoente) == type(""):
        print("Você precisa digitar um número, por favor! ")
    else:
        return base ** expoente

print(expo(5,8))

b = (int(input("Digite a base da operação: ")))

e = (int(input("Digite o expoente da operação: ")))

print(expo(b, e))