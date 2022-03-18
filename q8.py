from traceback import print_tb


print('Para o retângulo, digite 1')
print('Para o triângulo, digite 2')
print('Para o circulo, digite 3')
formaGeometrica = int(input())

num1 = 0
num2 = 0

if formaGeometrica == 1:
    print('Informe a altura')
    num1 = int(input())
    print('Informe o comprimento')
    num2 = int(input())
    print('Área:', num1 * num2)
else:
    if formaGeometrica == 2:
         print('Informe a altura')
         num1 = int(input())
         print('informe o valor da base')
         num2 = int(input())
         print('Área:', (num1 * num2) / 2)
    else:
        print('informe o valor do raio')
        num1 = int(input())
        print('Área:', 3.14 * num1**2 )