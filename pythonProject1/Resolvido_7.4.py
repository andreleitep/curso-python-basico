N = int(input('Quantidade de números: '))
Pos = []
Neg = []

for i in range(N):
    X = int(input(f'Escreva o elemento {i}: '))
    if X >= 0:
        Pos.append(X)
    else:
        Neg.append(X)
print('\nLista de números positivos:\n', Pos, f'\nContém {len(Pos)} elementos.')
print('\nLista de números negativos:\n', Neg, f'\nContém {len(Neg)} elementos.')