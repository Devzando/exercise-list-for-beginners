import random

nulos = random.randint(1, 9)
brancos = random.randint(1, 9)

naruto = ['naruto',random.randint(1, 9)]
sakura = ['sakura',random.randint(1, 9)]
shino = ['shino',random.randint(1, 9)]

candidatos = [naruto, sakura, shino]
vencedor = []

for i in candidatos:
    vencedor.append(i[1])

vencedor.sort()

for i in candidatos:
    if vencedor[-1] == i[1]:
        vencedor.clear()
        vencedor.append(i[0])

if(nulos + brancos >= naruto[1]+sakura[1]+shino[1]):
    print("Eleição inválida")
else:
    print("vencedor da eleição:", vencedor[0])