global x

# pascal 출력 데코레이터
def print_pascal(func):
    def func_event(*args):
        result = func(*args)
        global x
        string = " " * (x - len(result))
        for i in range(len(result)):
            string += str(result[i]) + " "
        print(string)

        return result
    return func_event
""" 겪고 있는 문제점 """
# 재귀 함수에 데코레이터 함수를 사용하면 어떻게 될까?
# 재귀를 할 때마다 데코레이터 함수가 호출된다.
# 새로운 응용 방법
# 출력되는 수열들을 데코레이터를 사용해서 값의 변화를 출력할 수 있지 않을까?
# 별찍기,피보나치 수열,파스칼의 삼각형 등등..
# 이에 관해 규칙 4번의 요소를 구현했다.

""" 현재 코드의 한계성 """
# 출력되는 파스칼의 요소가 10의자리가 넘어간다면 삼각형의 모양이 무너진다.
# 그렇다면 10의자리, 100의자리, 1000의 자리가 될것을 n == 1 일때 어떻게 판별할 것이고, 어떻게 값을 더해줄것인가?




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

# 규칙 4 공백 값 구하기, 출력되는 숫자 뒤에 공백이 따라 붙는다.
# 입력값이 n , 반복자 인덱스의 값을 i 라 지정할때, 왼쪽의 공백값은  x - i로 구할 수 있을 것 같다.
# i = 1  :    1
# i = 2  :   1 1
# i = 3  :  1 2 1
# i = 4  : 1 3 3 1
# i = 5  :1 4 6 4 1
# (x = 5) - (i = 1 )  = 4
# (x = 5) - (i = 2 )  = 3
# (x = 5) - (i = 3 )  = 2
# (x = 5) - (i = 4 )  = 1
# (x = 5) - (i = 5 )  = 0

# 이때 숫자가 들어갈 리스트, 공백이 들어갈 리스트를 본다면 다음 과 같다.
# i[5] =  ["1", " ", "4", " ", "6", " ", "4", " ", "1"]
# 홀수 일때는 리스트의 숫자가 출력되는데, 짝수일때는 공백이 출력된다, 별찍기와 굉장히 유사하다.
# 또한, 리스트의 길이는 (len(i) * 2) - 1을 한 것과 같다.
# 그런데 어짜피 반복문을 사용할 것, 리스트의 요소를 더해줄때마다 숫자뒤에 공백을 붙여주면 될 것 같다.



# 문제  : 입력값 n이 주어졌을때, n 번째 파스칼의 삼각형 리스트를 구하시오.

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
@print_pascal
def pascal(n):
    if n < 1:
        return "정확한 값을 입력해주세요."
    elif n == 1:
        return [1]
    else:
        temp_arr = pascal(n - 1)
        """실행 로직"""
        # n = 4
        # temp_arr = pascal(3)

        # n = 3
        # temp_arr = pascal(2)

        # n = 2
        # temp_arr = pascal(1)

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
        global x
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
# print(pascal(x))
# x = 5000
# 반복문 경과 시간 2.7514991760253906
# 재귀 경과 시간 2.7203762531280518

