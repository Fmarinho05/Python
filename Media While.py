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

# Serve para contar a qntd de vezes que a repetição vai acontecer.
contador = 0

# Serve para guardar as somas das notas fornecidas.
acumulador = 0

while(contador < quantidadeDeNotas):
   nota = int(input("Insira a nota " + str(contador + 1) + ": "))
   #nota = int(nota)

   acumulador = acumulador + nota
   contador = contador + 1

print(acumulador / quantidadeDeNotas)