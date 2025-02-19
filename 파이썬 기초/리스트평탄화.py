#리스트 평탄화
A= [1,2,[3,4],5,[6,7],[8,9]]
B = []
for a in A:
    if type(a) == list:
        # print(a)
        for i in a:
            B.append(i)
    else: B.append(a)
print(A)
print(B)