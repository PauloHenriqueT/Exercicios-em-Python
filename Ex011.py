l = float(input('Qual a largura da parede? '))
h = float(input('Qual a altura da parede? '))
a = l * h
print('A dimensao da parede é de {}x{} sua area é de {}㎡'.format(l, h, a))
tinta = a / 2
print('Voce precisa de {}L de tinta para pintar a parede'.format(tinta))