# print("""         ,r'"7
# r`-_   ,'  ,/
#  \. ". L_r'
#    `~\/
#       |
#       |""")

# #3003번 체스문제
# correct  = {
#     '킹':1, 
#     '퀸':1, 
#     '룩':2,
#     '비숍':2,
#     '나이트':2,
#     '폰':8
# }
# input_count = list(map(int, input().split()))
# A=[]*len(correct)
# # 결과 계산
# for i, piece in enumerate(['킹', '퀸', '룩', '비숍', '나이트', '폰']):
#     A.append(correct[piece] - input_count[i])
# print(*A)
# #for index, value in enumerate(iterable):
# # 인덱스와 값을 반환하는 enumerate

# #2444번 별찍기
# N = int(input())

# # 두 부분을 하나의 반복문으로 처리
# for i in range(1, N * 2):
#     if i <= N:
#         # 위쪽 부분: i는 1부터 N까지
#         print(" " * (N - i) + "*" * (2 * i - 1))
#     else:
#         # 아래쪽 부분: i는 N+1부터 2N-1까지
#         print(" " * (i - N) + "*" * (2 * (2 * N - i) - 1))

# #10988번 팰린드롬 (앞으로 뒤로 같은 글자)
# A=list(input())
# B=list(reversed(A))
# print(A)
# print(B)
# if A==B:
#     print(1)
# else: print(0)

# #1157번 단어공부
# #가장많이 사용된 알파벳 대문자로 출력. 여러개일땐 ? 출력
# from collections import Counter
# # 입력받은 단어
# word = input().upper()  # 대소문자 구분 없이 대문자로 변환
# # 알파벳 빈도 계산
# count = Counter(word)
# # 가장 많이 나온 알파벳을 찾음
# most_common = count.most_common(2)  # 두 번째로 많이 나온 알파벳까지 계산
# print(most_common)
# # 가장 많이 나온 알파벳이 여러 개 있는지 확인
# if len(most_common) > 1 and most_common[0][1] == most_common[1][1]:
#     print("?")
# else:
#     print(most_common[0][0])

# #크로아티아알파벳
# # 크로아티아 알파벳 리스트
# # 크로아티아 알파벳 리스트 (길이가 긴 알파벳부터 순서대로 처리)
# croatia_alphabets = ['dz=', 'c=', 'c-', 'd-', 'lj', 'nj', 'z=']

# # 입력받은 문자열
# word = input()

# # 크로아티아 알파벳을 하나의 문자로 취급하여 처리
# for alphabet in croatia_alphabets:
#     word = word.replace(alphabet, '*')  # 크로아티아 알파벳을 '*'로 대체
#     # print(word)
# # '*'로 대체된 문자열에서 알파벳 개수를 셈
# print(len(word))

# #1316번 그룹단어 체커
# def is_group_word(word): #bool자료형으로 이전문자 아니면 반환
#     seen = set() #등장했던 '알파벳'을 저장함. 순서구분x, 중복허용x (set의특성)
#     prev_char = '' #이전 문자 저장
    
#     for i in word:
#         if i != prev_char:      # 현재 문자가 이전 문자와 다를 때
#             if i in seen:       # 이미 등장한 문자라면 그룹 단어가 아님
#                 return False
#             seen.add(prev_char) # 이전 문자를 set에 추가
#         prev_char = i           # 이전 문자 갱신
#     return True

# N= int(input())
# count=0

# for i in range(N):
#     word = input().strip()
#     if is_group_word(word):
#         count += 1

# print(count)