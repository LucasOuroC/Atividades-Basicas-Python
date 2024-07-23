import random

list = [] 
orde = []
for i in range(4):
    nome = str(input("Digite o nome de quatro alunos para sorteio: "))
    list.append(nome)

s = random.choice(list)
print("O nome sorteado foi: {}".format(s))
