    #10807번 개수세기
N= int(input())
numbers = list(map(int, input().split()))
v = int(input())
answer = 0
for i in range(N):
    if numbers[i] == v:
        answer +=1
print(answer)