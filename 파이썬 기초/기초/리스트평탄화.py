# #리스트 평탄화
# A= [1,2,[3,4],5,[6,7],[8,9]]
# B = []
# for a in A:
#     if type(a) == list:
#         # print(a)
#         for i in a:
#             B.append(i)
#             # B +=[i]
#     else: 
#         B.append(a)
#         # B += [a]

# print(A)
# print(B)

A=[1,2,3,4,5]
output= 0
for a in A:
    output +=a
print(output)