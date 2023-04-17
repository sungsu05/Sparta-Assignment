# count
# 문자열 내에서 특정 문자가 몇개 있는지 세는 메서드
string = "hello python django!"
cnt = string.count('l')
print(cnt)
# 출력 : 2

################################################################################################
#find
# 문자열 내에서 특정 문자열이 처음 나오는 위치를 알려주는 메서드, 없을경우 -1을 반환

string = "hello python django!"
print(string.find('x'),string.find('l'))
# -1 2출력

################################################################################################
# index
string = "hello python django!"
try:
    print(string.index('x'))
except ValueError:
    print("ValueError!")
# ValueError! 출력

################################################################################################
# join
string = "hello python django!"
string_list = list(string)
result = "".join(string)
print(result)
# 원본 내용 출력

################################################################################################
# upper,lower
string = "hello python django!"
print(string.upper())
print(string.lower())
print(string.isupper()) # 대문자가 있다면 True 없으면 False
print(string.islower()) # 소문자가 있다면 True 없으면 False


################################################################################################
# replace
string = "hello python django!"
result = string.replace("django","student")
print(result)

################################################################################################
# split
string = "hello python django!"
result = string.split(' ')
print(result)

################################################################################################
# len
string = "hello python django!"
print(len(list(string)))
print(len(string))


################################################################################################
# len

numbers = [1,2,3,4,5]
del numbers[2]
# index 2 삭제
print(numbers)

################################################################################################
# append
numbers = [1,2,3,4,5]
numbers.append(6)
print(numbers)

################################################################################################
# sort,sorted

numbers = [1,5,3,2,7,9,5,1,3]
result = sorted(numbers)
print(result)
result = sorted(numbers,reverse=True)
print(result)
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)

################################################################################################
# list index

string_list = ["hello","python","django"]
print(string_list.index('python'))

################################################################################################
# list insert,remove,pop
numbers = [1,2,3,4,5,6,]
numbers.insert(2,9)
print(numbers)
numbers.remove(9)
print(numbers)
number = numbers.pop()
print(number,numbers)

################################################################################################
# list count

numbers = [1,2,3,4,5,6,2,3,3,3,3,8,9]
print(numbers.count(3))

################################################################################################
# list extend

numbers1 = [1,2,3,4,5]
numbers2 = [6,7,8,9,10]
print(numbers1+numbers2)
numbers1.extend(numbers2)
print(numbers1)


################################################################################################
# dict
product_price = {"모자":5000,"가방":10000,"신발":15000}
product_price.update({"필통":3000})
print(product_price)
del product_price['필통']
print(product_price)
print(list(product_price.keys()))
print(list(product_price.values()))
print(list(product_price.items())) # 튜플
product_price.clear()
print(product_price)

################################################################################################
# dict get
product_price = {"모자":5000,"가방":10000,"신발":15000}
print(product_price.get('모자'))
print(product_price.get('양말'))
print(product_price.get('양말','검색한 상품은 없습니다.'))
# 탐색값이 없으면 none을 반환하지만, 기본값을 설정할 수 있다.

################################################################################################
# dict in
key_down = 'w'
skill = {'q':'q스킬 발동','w':'w스킬 발동','e':'e스킬 발동','r':'r스킬 발동'}
print(key_down in skill) #True and False

