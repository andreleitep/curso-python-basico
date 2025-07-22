P = int(input('Digite o valor do primeiro termo P: '))
R = int(input('Digite o valor da razão R: '))
Q = int(input('Digite a quantidade de termos Q: '))
L = [P]
T = L[0]
while len(L) < Q:
    L.append(T + R)
    T = T + R
print('\n', L)
print('\nFim do Programa')