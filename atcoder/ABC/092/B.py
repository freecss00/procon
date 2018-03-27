n = int(input())
d, x = map(int, input().split())
a = [int(input()) for _ in range(n)]
ans = n + x
for ai in a:
    ans += (d - 1) // ai
print(ans)
