t = int(input())
for c in range(t):
  tmp = list(map(int, input().split()))
  n, scores = tmp[0], tmp[1:]
  average = sum(scores) / n
  students = sum(map(lambda x: x > average, scores))
  print(f'{students / n * 100:.3f}%')
