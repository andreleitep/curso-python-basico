X = int(input('Escreva o primeiro elemento: '))
L = []
while X != 0:
    L.append(X)
    X = int(input('Escreva mais um elemento: '))
print(f'\nLista resultante:\n {L} \nContém {len(L)} elementos.')
print('\nFim do Programa.')