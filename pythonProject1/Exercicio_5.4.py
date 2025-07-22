D = int(input('Digite o valor de D: '))
while D <= 0:
    D = int(input('Digite o valor de D: '))
i = 1
while i < 100:
    if i % D == 0:
        print(i, end = ', ')
    i += 1
print('\n\nFim do Programa')