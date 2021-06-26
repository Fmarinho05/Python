# #Input: Entrada de teclado para o usuário.

# import time

# quantidadeDeNotas = int(input("Quantas notas você gostaria de registrar ? "))
# #quantidadeDeNotas = int(quantidadeDeNotas)

# contador = 0

# while(contador < quantidadeDeNotas):
#     print(contador)
#     contador = contador + 1


# Serve para guarda a qntd de notas que eu quero colocar.
quantidadeDeNotas = int(input("Quantas notas você gostaria de registrar ? "))
#quantidadeDeNotas = int(quantidadeDeNotas)

# Contar a qntd as vezes que a repetição já aconteceu.
contador = 0

# Serve para guardar as somas das notas fornecidas.
acumulador = 0

while(contador < quantidadeDeNotas):
   nota = int(input("Insira a nota " + str(contador) + ": "))
   #nota = int(nota)
   acumulador = acumulador + nota
   contador = contador + 1

print(acumulador / quantidadeDeNotas)