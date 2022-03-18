nums = []
for i in range(3):
    print('informe um valor')
    num = int(input())
    nums.append(num)


if nums[0] == nums[1] + nums[2]:
    print('é um triângulo')
    if nums[0] == nums[1] and nums[0] == nums[2]:
        print('e é equilátero')
    else:
        if nums[0] == nums[1] or nums[0] == nums[2] or nums[1] == nums[2]:
            print('e é isósceles')
        else:
            print('e é escaleno')
else:
    print('não é um triângulo')