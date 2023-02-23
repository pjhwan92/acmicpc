calc = lambda x: (x % 10) * 10 + (((x // 10) + (x % 10)) % 10)
n = int(input())
cnt = 1
r = calc(n)
while r != n:
  cnt += 1
  r = calc(r)
print(cnt)
