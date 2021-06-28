#import: É uma biblioteca que já vem junto com o Python. 

import time

contador = 0

# Estruturas de repetição - WHILE: ENQUANTO
# O computador usar o sistema decimal de numeração, que começa apartir do: (0 1 2 3 4 5 6 7 8 9)


while(contador < 10 ):

 # Em Python eu posso usar uma variável, no corpo do print, mais de uma vez para finalidades diferente.

    print("Contador Binário: " + str(contador) + " Contador Numérico: " + str(contador + 1))
    time.sleep(1)
    contador = contador + 1

# Incremento a estrutura de repetição: ex: contador = contador + 1, para continuar contando e acrescentando mais 1 na estrutura. 