nums = []
for i in range(3):
    print('informe um valor')
    num = int(input())
    nums.append(num)


if nums[0]**2 == nums[1]**2 + nums[2]**2:
    print('é um triângulo retângulo')
else:
    print('não é um triângulo retângulo')