i = 0
while i < 25:
    i = i + 1
    if i % 4 == 0:
        print('__', end = '    ')
        continue
    print(i, end = '    ')