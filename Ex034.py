salario = float(input('Qual o sálario do funcionário: '))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('Quem ganha o valor de R${:.2f} passa a ganhar R${:.2f}'.format(salario, novo))