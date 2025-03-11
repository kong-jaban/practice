# #2738번
# #N*M크기의 두 행렬 A와 B가 주어졌을 때, 두 행렬을 더하는 프로그램을 작성하시오.
# N, M = map(int, input().split())

# # 첫 번째 행렬 입력
# matrix1 = []
# for i in range(N):
#     row = list(map(int, input().split()))  # 한 줄을 입력받고 공백으로 구분하여 정수 리스트로 변환
#     matrix1.append(row)  # 그 줄을 행렬에 추가
# # 두 번째 행렬 입력
# matrix2 = []
# for i in range(N):
#     row = list(map(int, input().split()))  # 두 번째 행렬 입력 받기
#     matrix2.append(row) # 행렬을 더한 결과 출력
# for i in range(N):
#     result = []
#     for j in range(M):
#         result.append(matrix1[i][j] + matrix2[i][j])  # 동일한 위치의 원소 더하기
#     print(*result)  # 결과 리스트 출력 (공백으로 구분)

# # # 2566번 최댓값 문제
# # # 9×9 격자판에 쓰여진 81개의 자연수 또는 0이 주어질 때, 이들 중 최댓값을 찾고
# # #  그 최댓값이 몇 행 몇 열에 위치한 수인지 구하는 프로그램을 작성
# rows=[]

# for i in range(9):
#     row=list(map(int, input().split()))
#     rows.append(row)
#     # print(rows)

# max_value = -1
# max_position = (0, 0)  # 최댓값의 위치 (행, 열)
# for i in range(9):
#     for j in range(9):
#         if rows[i][j] > max_value:
#             max_value = rows[i][j]
#             max_position = (i+1, j+1)

# print(max_value)
# print(max_position[0], max_position[1]) 

# #10798번 세로읽기

# rows = []  # 입력 받은 배열을 저장할 리스트
# news = [[" " for _ in range(5)] for _ in range(15)]  # 최대 15개의 행과 5개의 열로 이루어진 배열 생성

# # 5개의 행 입력 받기
# for i in range(5):
#     row = list(input())  # 한 줄씩 입력받고 문자로 이루어진 리스트로 변환
#     rows.append(row)

# # 세로로 읽어서 새로운 배열(news)에 저장
# for i in range(15):  # 최대 15개의 행에 대해
#     for j in range(5):  # 5개의 열에 대해
#         if i < len(rows[j]):  # 현재 열의 문자열 길이를 넘지 않으면
#             news[i][j] = rows[j][i]  # 세로로 읽어 news 배열에 저장

# # 결과 출력
# for row in news:
#     print("".join(row)) 

# # 2563번 색종이문제

# #입력받기(색종이 수, 두개의 자연수)
# N=int(input())
# paper = [[0] * 100 for i in range(100)]
# #검정 정사각형 모양대로 모양 넣기
# for i in range(N):
#     A, B = map(int, input().split())
#     for i in range(A, A+10):
#         for j in range(B, B+10):
#             paper[i][j]=1
# count = 0
# for row in paper:
#     count += sum(row)

# # 결과 출력
# print(count)