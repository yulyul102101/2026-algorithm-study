for i in range(2992, 10000):
    a = i
    b = i
    v = i
    suma = 0
    sumb = 0
    sumc = 0

    while(a // 10 != 0):
        suma += a % 10
        a //= 10
    suma += a % 10

    while(b // 12 != 0):
        sumb += b % 12
        b //= 12
    sumb += b % 12

    while(v // 16 != 0):
        sumc += v % 16
        v //= 16
    sumc += v % 16

    if suma == sumb == sumc:
        print(i)
