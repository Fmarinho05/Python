#Vetores são um conjuntos de dados ordenados. Chamado de 'list' no Python.  

Class: Tuple - É semelhante a uma 'list', entretanto, com a característica principal de ser imutável.
nomes = ("Felipe", "Lucas", "Rafael")
print (type(nome))


Class: List - É conjunto de dados ordenados. Que de qualquer ponto do programa pode ser mudada ou acrescentada.
nomes = ["Felipe", "Rafael", "Adriene"]
# print (type(nomes))

# Criando um vetor, acrecentando e acessando seus índices ao longo do código.
nomes = []
print(nomes)

nomes.append("Felipe")

print(nomes)

nomes.append("Rafael")

print(nomes)

nomes.append("Adriene")

print(nomes)

print(nomes[0])

nomes = ["Felipe", "Rafael", "Adriene"]

for cliente in nomes:
    print(cliente)
