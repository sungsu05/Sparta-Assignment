# 첫 번째 문제
# def solution(sizes):
#     x_max,y_max = -1,-1
#     for i in range(len(sizes)):
#         # 가로값을 최대값으로 몰아주기
#         if(sizes[i][0] < sizes[i][1]):
#             sizes[i][0], sizes[i][1] = sizes[i][1] ,sizes[i][0] #swap
#         # 최대값 탐색
#         if sizes[i][0] > x_max:
#             x_max = sizes[i][0]
#         if sizes[i][1] > y_max:
#             y_max = sizes[i][1]
#
#     return x_max*y_max

################################# 코드 축약 #################################
# def solution(sizes):
#     x_max,y_max = -1,-1
#     for x,y in sizes:
#         if x < y:
#             x,y= y,x
#         if x > x_max:
#             x_max = x
#         if y > y_max:
#             y_max = y
#     return x_max*y_max
################################# 코드 축약 #################################
def solution(sizes):
    x_max,y_max = -1,-1
    for x,y in sizes:
        if x < y:
            x,y= y,x
        x_max = max(x_max,x)
        y_max = max(y_max,y)
    return x_max*y_max

arr =[[60, 50], [30, 70], [60, 30], [80, 40]]
print(solution(arr))
arr = [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]
print(solution(arr))
arr = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]
print(solution(arr))



# 두 번째 문제

def solution(angle):
    if angle <= 90:
        return 1 if angle<90 else 2
    return 4 if(angle==180) else 3

print(solution(70))
print(solution(91))
print(solution(180))


# 세 번째 문제

print("""\\    /\\
 )  ( ')
(  /  )
 \\(__)|
""")