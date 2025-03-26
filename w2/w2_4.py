import sys

# 입력 받기
N, K = map(int, sys.stdin.readline().split())
wheel = ['?'] * N  # 바퀴 초기화
used = set()  # 이미 사용된 알파벳 저장

position = 0  # 화살표가 가리키는 위치

for _ in range(K):
    S, C = sys.stdin.readline().split()
    S = int(S)  # 시계 방향으로 회전하는 횟수

    position = (position - S) % N  # 시계 방향 회전

    # 충돌 검사
    if wheel[position] == '?':  # 빈 자리라면 알파벳 채우기
        if C in used:  # 이미 사용된 알파벳이라면 불가능한 경우
            print("!")
            sys.exit()
        wheel[position] = C
        used.add(C)
    elif wheel[position] != C:  # 다른 알파벳이 이미 있으면 불가능
        print("!")
        sys.exit()

# 바퀴를 현재 화살표 위치에서 역순으로 출력
result = ''.join(wheel[position:] + wheel[:position])
print(result)
