X = int(input('Digite o valor de X: '))
R = 0
i = 0
while X != 0:
    R += X
    i += 1
    X = int(input('Digite o valor de X: '))
print(f'O valor total é {R} \n    Você digitou {i} valores.')