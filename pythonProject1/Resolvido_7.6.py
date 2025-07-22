X = int(input('Escreva o primeiro elemento: '))
L = []
while X != 0:
    if X not in L:
        L.append(X)
    else:
        print(f'    Erro. O valor {X} já está na lista')
    X = int(input('Escreva mais um elemento: '))
L.sort()
print(f'\nLista resultante:\n {L} \nContém {len(L)} elementos.')
print('\nFim do Programa.')