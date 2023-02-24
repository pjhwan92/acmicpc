first = int(input())
second = input().strip()

result = 0
multiplier = 1
for i in reversed(second):
  n = int(i)
  step_result = first * n
  print(step_result)
  result += step_result * multiplier
  multiplier *= 10
print(result)
