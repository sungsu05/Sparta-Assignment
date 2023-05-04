# json.lods:
# json 문자열을 python 객체,딕셔너리로 변환

import json

# JSON 문자열
json_data = '{"name": "John", "age": 30, "city": "New York"}'

# JSON 문자열을 Python 객체로 변환
data = json.loads(json_data)

# Python 객체 출력
print(data)
print(type(data))

# {
# "employee": {
# "name": "sonoo",
# "salary": 56000,
# "married": true
# }
# }

# json.load : json 파일을 python 객체(딕셔너리)로 변환
with open('data.json') as file:
    data = json.load(file)

print(data)
print(type(data))


with open('data.json') as file:
    data = json.load(file)
print(data['employee'])
print(data['employee']['name'])
print(data['employee']['salary'])

# json.dump : python 객체를 json 파일로 변환

# Python 객체
data = {'name': 'John', 'age': 30, 'city': 'New York'}

# Python 객체를 JSON 파일로 변환
with open('data2.json', 'w') as file:
    json.dump(data, file)

# 동기화 await
# 파일 쓰기 코드 / 파일 작업 코드

