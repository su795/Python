"""
    날짜 : 2020/06/23
    이름 : 오세훈
    내용 : if문 교재 p117
"""

# if
num1, num2 = 1, 2


if num1 >= 1:
    print('num1은 1보다 크거나 같다.')

if num2 < 1:
    print('num2는 1보다 작다.')

if num1 >= 1:
    if num2 >= 2:
        print('num1은 1보다 크고 num2는 2보다 크다.')

if num1 >= 1 and num2 >= 2:
    print('num1은 1보다 크고 그리고 num2는 2보다 크다.')

# if ~ else
num3, num4 = 3, 4

if num3 > num4:
    """   참 일경우 """
    print('num3이 num4보다 크다.')
else:
    """ 거짓 일경우 """
    print('num3이 num4보다 작다.')



# if ~ elif ~ else
if num1 > num2:
    print('num1은 num2보다 크다.')
elif num2 > num3:
    print('num2이 num3보다 크다.')
elif num3 > num4:
    print('num3이 num4보다 크다.')
else:
    print('num4가 제일 크다.')


# 연습문제
score = 86
if 90 <= score <= 100:
    print('A입니다.')
elif score >= 80 and score < 90:
    print('B입니다.')
elif 70 <= score < 80:
    print('C입니다.')
elif 60 <= score < 70:
    print('D입니다.')
else:
    print('F입니다.')


