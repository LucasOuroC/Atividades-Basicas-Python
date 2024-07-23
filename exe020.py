import random

list = [] 
orde = []
for i in range(4):
    nome = str(input("Digite o nome de quatro alunos para sorteio: "))
    list.append(nome)

print("A ordem de sorteio é: ")
for i in range(4):
    s = str(random.choice(list))
    orde.append(s)
    list.remove(s)
    
print(orde)