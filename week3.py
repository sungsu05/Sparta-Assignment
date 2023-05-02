import time
# 시간 측정 데코레이터 함수
def print_time(func):
    def func_event(*args):
        start_time = time.time()
        result = func(*args)
        end_time = time.time() - start_time
        # print(f"경과시간 = {end_time}")
        print(f"경과시간 = {end_time}\n{result}")
        return result
    return func_event
""" 겪고 있는 문제점 """
# 재귀 함수에 데코레이터 함수를 사용하면 어떻게 될까?
# 나의 예상 : 재귀를 할 때마다 데코레이터 함수가 호출된다.  아니라면 한번만
# 실제 출력 : 재귀를 할 때마다 데코레이터 함수가 호출 되는 것이 아니며 출력 값이 두번 나오는 의아한 결과 값이 나왔다.






""" 문제의 규칙 찾기 """
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

@print_time
def solution(n):
    if n < 1:
        return "정확한 값을 입력해주세요."
    elif n < 3 :
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


## 코드 발전, 재귀 함수를 이용
@print_time
def pascal(n):
    if n < 1:
        return "정확한 값을 입력해주세요."
    elif n == 1:
        return [1]
    else:
        temp_arr = pascal(n - 1)
        """실행 로직"""
        # n = 4
        # temp_arr = solution(3)

        # n = 3
        # temp_arr = solution(2)

        # n = 2
        # temp_arr = solution(1)

        # n = 1
        # return [1] >> n이 2일때로 재귀

        # n = 2
        # temp_arr = [1]
        # result = [1] * n = [1,1]
        # for i in range(0,n-1) : (0,1)
        #   i = 0 > contionue
        #   i = 1 > for문 종료
        # return [1,1]  >> n이 3일때로 재귀

        # n = 3
        # temp_arr = [1,1]
        # result = [1] * n = [1,1,1]
        # for i in range(0,2)
        # i = 0 > continue
        # i = 1 > result[1] = temp_arr[0] + temp_arr[1]  >> result[1] = 1 + 1
        # i = 2 > for문 종료 , 결과값.  result = [1,2,1]

        # n = 4
        # temp_arr = [1,2,1]
        # result = [1] * n = [1,1,1,1]
        # for i in range(0,3)
        # i = 0 > continue
        # i = 1 > result[1] = temp_arr[0] + temp_arr[1]  >> result[1] = 1 + 2
        # i = 2 > result[2] = temp_arr[1] + temp_arr[2]  >> result[2] = 2 + 1
        # i = 3 > for문 종료, 결과값. result = [1,3,3,1]

        result = [1] * n
        for i in range(1, n - 1):
            """ 새로운 리스트 만들기 """
            # if i == 0 or i == n-1 :
            #     continue
            # for 반복문의 시작값 1, 종료값을 n-1로 지정했으며,
            # 초기값을 1*n의 리스트로 만들어 if문으로 검증할 필요 없음

            result[i] = temp_arr[i-1] + temp_arr[i]
        return result

while True:
    try:
        x = int(input())
        break
    except TypeError:
        print("정수형 숫자를 입력해주세요.")
    except ValueError:
        print("정수형 숫자를 입력해주세요.")

# 반복문
# print(solution(x))
# solution(x)

# 재귀 함수
# print(pascal(x))
pascal(x)

# x = 5000
# 반복문 경과 시간 2.7514991760253906
# 재귀 경과 시간 2.7203762531280518
