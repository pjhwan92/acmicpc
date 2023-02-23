pieces = [1, 1, 2, 2, 2, 8]
actual = list(map(int, input().split()))

for p, a in zip(pieces, actual):
  print(p - a, end=' ')
