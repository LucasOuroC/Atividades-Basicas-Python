from math import sqrt
o = float(input("Digite o comprimento do cateto oposto em metros: "))
a = float(input("Digite o comprimento do cateto adjacente em metros: "))

h = sqrt((o**2) + (a**2))

print("O comprimento da hipotenusa é de {:.2f} metros".format(h))
