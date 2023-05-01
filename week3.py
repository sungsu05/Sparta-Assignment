# 파스칼의 삼각형

# n = 1  :         1
# n = 2  :        1 1
# n = 3  :       1 2 1
# n = 4  :      1 3 3 1
# n = 5  :     1 4 6 4 1
# n = 6  :    1 5 10 10 5 1
#     x =     0 1 2  3  4 5

# 규칙 1. 가로 폭의 길이 =  n
# 규칙 2. 테두리, arr[0], arr[-1] =  1

# n = 1 :  1
# n = 2 :  1 1
# n = 3 :  1 2 1
# n = 4 :  1 3 3 1
# n = 5 :  1 4 6 4 1
#     x =  0 1 2 3 4

# 규칙 3 현재 만들어야 하는 리스트를 arr , 이전에 만든 리스트를 temp arr로 정의
# arr[0],arr[-1]을 제외한 x index의 값은 temp_arr[x-1] + temp_arr[x]


# 문제  : 입력값 n이 주어졌을때, n 번째 파스칼의 삼각형 리스트를 구하시오.

def solution(n):
    if 3 > n :
        return [1] if n == 1 else [1,1]
    index = 2
    temp_arr = [1,1]
    arr = temp_arr
    while n > index:
        index += 1
        arr = [0] * index
        for x in range(index):
            if x == 0:
                arr[0] = 1
            elif x == index -1:
                arr[index-1] = 1
            else :
                arr[x] = temp_arr[x-1] + temp_arr[x]
        temp_arr = arr
    return arr

x = 6
print(solution(x))

## 코드 발전, 재귀 함수를 이용

# def pascal(x):
#     pass
#
#
# def solution_2(n):
#     if 3 > n :
#         return [1] if n == 1 else [1,1]
#     index = 2
#     temp_arr = [1,1]
#     arr = temp_arr
#     while n > index:
#         index += 1
#         arr = [0] * index
#         arr = pascal(index)
#         temp_arr = arr
#     return arr
#
# x = 6
# print(solution(x))