A = int(input('Escreva um valor: '))
B = int(input('Escreva outro valor: '))
if A > B:
    print(f'O menor número é {B}')
elif B > A:
    print(f'O menor número é {A}')
else:
    print(f'Os dois números são iguais e valem {A}')