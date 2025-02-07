import pandas as pd
import numpy as np
from faker import Faker

fake = Faker()
num_records = 100000  # 예시 데이터 크기

# 데이터 생성 함수
def generate_data(num_records):
    data = []
    for i in range(num_records):
        record = {
            "id": i + 1,  # 고유한 ID 생성
            "name": fake.name(),
            "address": fake.address(),
            "email": fake.email(),
            "phone_number": fake.phone_number(),
            "job": fake.job(),
            "company": fake.company(),
            "birthdate": fake.date_of_birth(),
            "text": fake.text(),
        }
        data.append(record)
    return data

# 데이터프레임 생성
data = generate_data(num_records)
df = pd.DataFrame(data)

# CSV 파일 저장
df.to_csv('large_dataset.csv', index=False)
print("CSV 파일 생성 완료: large_dataset.csv")
