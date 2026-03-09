from random import randint
computador = randint(0, 5)
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print('Vou pensar em um numero entre 0 e 5 tente advinhar...')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
jogador = int(input('Em que número eu pensei? '))
if jogador == computador:
    print('Parabens, você consegui acertar o número que eu estava pensando! ')
else:
    print('Que pena você errou, eu tinha pensado no número {} '.format(computador))