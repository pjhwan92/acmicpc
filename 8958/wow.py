t = int(input())

for i in range(t):
  s = input()
  score = cur_score = 0
  for p in s:
    if p == 'O':
      cur_score += 1
      score += cur_score
    else:
      cur_score = 0
  print(score)
