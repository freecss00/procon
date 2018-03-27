n, k = map(int, input().split())
ans = 0
if k == 0:
    ans = n * n
else:
    for b in range(k+1, n+1):
        p, r = n // b, n % b
        ans += p * max(0, b - k) + max(0, r - k + 1)
print(ans)
