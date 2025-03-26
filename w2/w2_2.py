from collections import deque

# 입력 받기
N, K = map(int, input().split())

# 1부터 N까지의 사람을 deque로 초기화
dq = deque(range(1, N + 1))
result = []  # 제거된 순서를 저장할 리스트

while dq:
    dq.rotate(-(K - 1))  # K-1번 왼쪽으로 회전하여 K번째 요소가 맨 앞으로 오게 함
    result.append(dq.popleft())  # 제거된 사람을 결과 리스트에 추가

# 결과 출력
print("<" + ", ".join(map(str, result)) + ">")
