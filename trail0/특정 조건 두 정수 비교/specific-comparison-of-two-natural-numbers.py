A, B = map(int, input().split())

# 첫 번째 조건: A < B 인지 확인
if A < B:
    res1 = 1
else:
    res1 = 0

# 두 번째 조건: A == B 인지 확인
if A == B:
    res2 = 1
else:
    res2 = 0

# 두 결과값을 공백을 사이에 두고 출력
print(res1, res2)