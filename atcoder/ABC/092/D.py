h, w = 100, 100
ans = [[0] * w for i in range(h)]
a, b = map(lambda x: int(x) - 1, input().split())
table = [['.' if i % 2 == 0 else '#' for i in range(w)] for j in range(h)]
for i in range(w):
    table[0][i] = '.'
    table[99][i] = '#'

for i in range(0, 98, 2):
    for j in reversed(range(1, 98, 2)):
        if a == 0:
            break
        table[j][i] = '#'
        a -= 1
    else:
        continue
    break

for i in reversed(range(1, 100, 2)):
    for j in range(2, 99, 2):
        if b == 0:
            break
        table[j][i] = '.'
        b -= 1
    else:
        continue
    break

print(h, w)
print('\n'.join([''.join(t) for t in table]))
