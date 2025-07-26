def division_by_zero(A, B):
    if B == 0:
        raise ZeroDivisionError("Divisão por zero detectada.")
    R = A / B
    print(R)

Aa = int(input("Digite o valor de A: "))
Bb = int(input("Digite o valor de B: "))
division_by_zero(Aa, Bb)