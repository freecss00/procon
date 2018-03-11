# C - March
import collections
import itertools

n = int(input())
s = collections.defaultdict(int)
for i in range(n):
    s[input()[0]] += 1

seq = list(itertools.combinations(['M', 'A', 'R', 'C', 'H'], 3))
ans = 0
for l in seq:
    ans += s[l[0]] * s[l[1]] * s[l[2]]
print(ans)
