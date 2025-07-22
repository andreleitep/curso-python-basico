from random import randint
# Criação da lista
Qtde = int(input('Escreva a quantidade de números na lista: '))
L = []
for i in range(Qtde):
    L.append(randint(1, 30))
print(L, '\n')
# Pesquisa na lista
consulta = int(input('Procure um número na lista: '))
while consulta > 0:
    if consulta in L:
        print(f'    Há {L.count(consulta)} ocorrência(s) de {consulta} na lista.\n')
    else:
        print(f'    O número {consulta} não está na lista.\n')
    consulta = int(input('Procure um número na lista: '))
print('\nFim do programa')