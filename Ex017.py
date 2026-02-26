import math
cato = float(input('Digite o valor do cateto oposto: '))
cata = float(input('Digite o valor do cateto adjacente: '))
hi = math.hypot(cato, cata)
print("A hipotenusa vai medir {:.2f}".format(hi))