from math import sqrt

get_min_max_coord = lambda nums: ((min(nums[0], nums[2]), min(nums[1], nums[3])), (max(nums[0], nums[2]), max(nums[1], nums[3])))

for i in range(4):
  nums = list(map(int, input().split()))
  rect_a = get_min_max_coord(nums[:4])
  rect_b = get_min_max_coord(nums[4:])
  distance_x = abs((rect_a[0][0] + rect_a[1][0]) - (rect_b[0][0] + rect_b[1][0]))
  distance_y = abs((rect_a[0][1] + rect_a[1][1]) - (rect_b[0][1] + rect_b[1][1]))
  extend_x = rect_a[1][0] - rect_a[0][0] + rect_b[1][0] - rect_b[0][0]
  extend_y = rect_a[1][1] - rect_a[0][1] + rect_b[1][1] - rect_b[0][1]

  if distance_x == extend_x and distance_y == extend_y:
    print('c')
  elif (distance_x == extend_x and distance_y < extend_y) or (distance_x < extend_x and distance_y == extend_y):
    print('b')
  elif distance_x > extend_x or distance_y > extend_y:
    print('d')
  else:
    print('a')
