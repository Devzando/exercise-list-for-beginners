print('Informe o valor da temperatura em que se encontra a água')
temp = int(input())

if temp < 0:
    print('Água se encontra no estado sólido')
else:
    if temp >= 0 and temp <= 100:
         print('Água se encontra no estado líquido')
    else:
        print('Água se encontra no estado gasoso')