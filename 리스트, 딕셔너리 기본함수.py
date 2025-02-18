a= [52,263, 32, 103,53]
print(max(a))
print(min(a))
print(max(*a))
print(sum(a))
a= range(0,10)
for i in reversed(a):
    print(i)

#enumerate() 함수
fruits = ["바나나", "사과", "포도"]
i =0
for fruit in fruits:
    print(fruit)

#enumerate() 사용시 > [(), (), ()] 형태 (튜플)
for fruit in enumerate(fruits):
    print(fruit[0], fruit[1])

# 형식 
# for 인덱스, 값 in enumerate(리스트)
for i, fruit in enumerate(fruits):
    print(i, fruit)


#items()함수
a= {
    "이름":"바나나",
    "가격": 1500,
    "원산지":"말레이시아"

}
for k, v in a.items():
    print(k, v)