# 파일을 쓰기 모드로 엽니다.
file = open("example.txt", "w")

# 파일에 데이터를 작성합니다.
file.write("Hello, world!\n")
file.write("This is an example file.\n")
file.write("Writing some lines.\n")

# 파일을 닫습니다.
file.close()

# 파일을 읽기 모드로 열고 데이터를 읽는 예제입니다.
file = open("example.txt", "r")

# 파일 전체를 읽어옵니다.
contents = file.read()
print("전체 내용:")
print(contents)

# 파일을 닫습니다.
file.close()

# 파일을 다시 읽기 모드로 열고 한 줄씩 읽는 예제입니다.
file = open("example.txt", "r")

print("한 줄씩 읽기:")
# 파일의 각 줄을 반복하며 읽어옵니다.
for line in file:
    print(line.strip())

# 파일을 닫습니다.
file.close()

# 파일을 읽기 모드로 열고 모든 줄을 읽어 리스트로 반환하는 예제입니다.
file = open("example.txt", "r")

lines = file.readlines()
print("리스트로 읽기:")
print(lines)

# 파일을 닫습니다.
file.close()