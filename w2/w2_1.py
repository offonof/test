from collections import deque

# 입력 받기
N, M = map(int, input().split())  # N: 큐의 크기, M: 뽑아야 할 원소 개수
targets = list(map(int, input().split()))  # 뽑아야 할 원소의 위치

# 덱 초기화
dq = deque(range(1, N + 1))  
count = 0  # 이동 횟수

for target in targets:
    idx = dq.index(target)  # 현재 큐에서 목표 원소의 위치
    
    # 왼쪽 이동이 빠른 경우
    if idx < len(dq) - idx:
        dq.rotate(-idx)  # 왼쪽으로 회전
        count += idx
    else:
        dq.rotate(len(dq) - idx)  # 오른쪽으로 회전
        count += (len(dq) - idx)
    
    dq.popleft()  # 첫 번째 원소 제거

print(count)
