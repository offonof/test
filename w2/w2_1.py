"""
지민이는 N개의 원소를 포함하고 있는 양방향 순환 큐를 가지고 있다. 지민이는 이 큐에서 몇 개의 원소를 뽑아내려고 한다.

지민이는 이 큐에서 다음과 같은 3가지 연산을 수행할 수 있다.

첫 번째 원소를 뽑아낸다. 이 연산을 수행하면, 원래 큐의 원소가 a1, ..., ak이었던 것이 a2, ..., ak와 같이 된다.
왼쪽으로 한 칸 이동시킨다. 이 연산을 수행하면, a1, ..., ak가 a2, ..., ak, a1이 된다.
오른쪽으로 한 칸 이동시킨다. 이 연산을 수행하면, a1, ..., ak가 ak, a1, ..., ak-1이 된다.
큐에 처음에 포함되어 있던 수 N이 주어진다. 그리고 지민이가 뽑아내려고 하는 원소의 위치가 주어진다. 
(이 위치는 가장 처음 큐에서의 위치이다.) 
이때, 그 원소를 주어진 순서대로 뽑아내는데 드는 2번, 3번 연산의 최솟값을 출력하는 프로그램을 작성하시오.
"""

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
