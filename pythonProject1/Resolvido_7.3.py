N = int(input('Quantidade de números: '))
L = []
for y in range(N):
    X = float(input(f'Elemento {y}: '))
    L.append(X)
print('\nResultado')
for valor in L:
    print(f'{valor:.2f}')

print('Fim do programa.')