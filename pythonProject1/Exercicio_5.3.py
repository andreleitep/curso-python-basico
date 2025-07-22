print('Progressão Aritmética (PA)')
P = int(input('Digite o primeiro termo: '))
R = int(input('Digite a razão: '))
i = 0
while i < 10:
    print(f'{i+1}º termo: {P + R * i}', end = ', ')
    i += 1
print('\n\n    Fim do Programa')