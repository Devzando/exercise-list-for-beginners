print("Para sexo Masculino, digite 1")
print("Para sexo Feminino, digite 2")
sexo = int(input())
print("informe a sua altura")
altura = float(input())

if(sexo == 1):
     print((72.2 * altura) -58)
else:
    print((62.1 * altura) -44.7)