n = int(input())
a = [0] + list(map(int, input().split())) + [0]
dist = 0
for i in range(len(a) - 1):
    dist += abs(a[i] - a[i + 1])

for i in range(len(a) - 2):
    d1, d2 = a[i+1] - a[i], a[i+2] - a[i]
    if abs(d1) + abs(d2) == abs(d1 - d2):
        print(dist - 2 * abs(d1))
    elif 0 < d2 < d1:
        print(dist - 2 * abs(d1 - d2))
    elif d1 < d2 < 0:
        print(dist - 2 * abs(d1 - d2))
    else:
        print(dist)
