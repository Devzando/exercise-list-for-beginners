print("Para escolher o veículo Morcego preto, digite 1")
print("Para escolher o veículo Vampiro voador, digite 2")
carro = int(input())

if(carro == 1):
    print((295 / 16) * 0.75 + 300 )
else:
    print((295 / 11) * 0.75 + 500)