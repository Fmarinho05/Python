# Variáveis recebem os valores...

#Input: Entrada de teclado para o usuário.

# nota1 = input("Insira a primeira nota: ")
# nota2 = input("Insira a segunda nota: ")
# nota3 = input("Insira a terceira nota: ")

# #print(type (nota1), type(nota2), type(nota3)) - 'str'

# intnota1 = int(nota1)
# intnota2 = int(nota2)
# intnota3 = int(nota3)

#print( type (intnota1), type (intnota2), type (intnota3)) - 'int'

# A variável media recebe o calculo da média das três notas.

#media = (intnota1 + intnota2 + intnota3) / 3

# nota1 = input("Insira a primeira nota: ")
# nota2 = input("Insira a segunda nota: ")
# nota3 = input("Insira a terceira nota: ")

# nota1 = int(nota1)
# nota2 = int(nota2)
# nota3 = int(nota3)

# A variável media recebe o calculo da média das três notas.

#media = (nota1 + nota2 + nota3) / 3

nota1 = int(input("Insira a primeira nota: "))
nota2 = int(input("Insira a segunda nota: "))
nota3 = int(input("Insira a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

 # Estrututa de decisão que decide se o aluno está aprovado ou não.

# if(media >= 70):
#     print("Boas férias, você está aprovado.")

# elif(media >= 50):
#     print("Você está de recuperação.")

# else:
#     print("Reprovado.")


# Adaptações para tipos de 'Strings templates'

if(media >= 70):
    print("A sua média foi " + str (media) + ". Boas férias.")

elif(media >= 50):
    print("A sua média foi %d. Você está de recuperação." % media)

else:
    print(f"A sua média foi {int(media)}. Você está reprovado.")