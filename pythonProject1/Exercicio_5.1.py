x = int(input('Digite o valor de x: '))
while x != 0:
    if x % 2 == 0:
        print(f'{x} é par')
    else:
        print(f'{x} é impar')
    x = int(input('Digite o valor de x: '))
print('\nFim do programa')