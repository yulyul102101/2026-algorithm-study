import sys

reverse1 = {
    '@': 'a',
    '[': 'c',
    '!': 'i',
    ';': 'j',
    '^': 'n',
    '0': 'o',
    '7': 't',
}

n = int(sys.stdin.readline())
words = [sys.stdin.readline().strip() for _ in range(n)]

for word in words:
    i = 0
    changed = 0
    result = []

    while i < len(word):
        if i + 2 < len(word) and word[i:i+3] == "\\\\'":
            result.append('w')
            changed += 1
            i += 3
        elif i + 1 < len(word) and word[i:i+2] == "\\'":
            result.append('v')
            changed += 1
            i += 2
        elif word[i] in reverse1:
            result.append(reverse1[word[i]])
            changed += 1
            i += 1
        else:
            result.append(word[i])
            i += 1

    decoded = "".join(result)

    if changed * 2 >= len(decoded):
        print("I don't understand")
    else:
        print(decoded)
