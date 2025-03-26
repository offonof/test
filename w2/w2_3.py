from collections import deque

# 입력 받기
N = int(input())
balloons = list(map(int, input().split()))

# deque 초기화 (번호, 값) 형태로 저장
dq = deque(enumerate(balloons, start=1))  # (풍선 번호, 종이의 숫자)

result = []

while dq:
    idx, value = dq.popleft()  # 현재 풍선 터뜨리기
    result.append(idx)  # 터진 풍선 번호 저장

    if not dq:  # 모든 풍선을 터뜨렸다면 종료
        break

    if value > 0:
        dq.rotate(-(value - 1))  # 양수 이동 (현재 풍선 제외하고 이동)
    else:
        dq.rotate(-value)  # 음수 이동 (그대로 회전)

# 결과 출력
print(" ".join(map(str, result)))
