def solution(polynomial):
    ts = polynomial.split(" + ")
    x = 0
    cnst = 0

    for t in ts:
        if 'x' in t:
            if t == 'x':
                x += 1
            else:
                x += int(t.replace('x',''))
        else:
            cnst += int(t)

    if x and cnst:
        return f'{"x" if x == 1 else str(x)+"x"} + {cnst}'
    elif x:
        return "x" if x == 1 else f'{x}x'
    else:
        return str(cnst)