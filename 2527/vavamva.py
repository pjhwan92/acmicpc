# 거리로

    #  좌하 ,  좌상  ,  우하 ,  우상
    # (x, y), (x, q), (p, y), (p, q)
"""
x, q +---+ p, q
     |   |
     |   |
x, y +---+ p, y     
"""

for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())

    px_1 = p1 - x1
    qy_1 = q1 - y1

    px_2 = p2 - x2
    qy_2 = q2 - y2

    middle_1 = [(px_1) / 2 + x1, (qy_1) / 2 + y1]  # 1번 사각형의 무게중심
    middle_2 = [(px_2) / 2 + x2, (qy_2) / 2 + y2]  # 2번 사각형의 무게중심

    # "무게중심간 x좌표차이, y좌표 차이" 와 "사각형의 가로, 세로 길이" 를 비교해줌
    
    # 선분에서든 점에서든 만나면 조건에 걸림
    if abs(middle_1[0] - middle_2[0]) > (px_1 + px_2) / 2 or abs(middle_1[1] - middle_2[1]) > (qy_1 + qy_2) / 2:
        print('d')

    # 둘 다 만족하면 점에서 만남
    elif abs(middle_1[0] - middle_2[0]) == (px_1 + px_2) / 2 and abs(middle_1[1] - middle_2[1]) == (qy_1 + qy_2) / 2:
        print('c')
    
    # 둘 중 하나만 만족하면 선에서 만남 (둘 다 만나는 조건은 위에서 걸림)
    elif abs(middle_1[0] - middle_2[0]) == (px_1 + px_2) / 2 or abs(middle_1[1] - middle_2[1]) == (qy_1 + qy_2) / 2:
        print('b')
    
    # 위 조건들 다 제외하면 교집합이 생김
    else:
        print('a')