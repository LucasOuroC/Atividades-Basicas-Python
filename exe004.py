n = input('Digite algo: ')

print('O tipo primitivo é: ', type(n))
print('Tem espaços? ', n.isspace())
print("É um numero?", n.isnumeric())
print("É alfabetico?", n.isalpha())
print("Esta em maiusculo?", n.isupper())
print("Esta em minusculas?", n.islower())
print("Esta capitalizada?", n.istitle())
