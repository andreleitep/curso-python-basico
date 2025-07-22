X = 1
while X > 0:
    X = int(input('Digite X: '))
    if X == 0:
        print('    você digitou zero...')
        break       # Se passar pelo break, não passa pelo else, sai direto do while.
    print(X)
else:
    print('    você digitou negativo...')

print('Fim do Programa')