fra = str(input('Digite uma frase: ')).upper()
print('A letra A aparece {} vezes na frase'.format(fra.count('A')))
print('A primeira letra A apareceu na posiçao {}'.format(fra.find('A')+1))
print('A última letra A apareceu na posiçao {}'.format(fra.rfind('A')+1))
