"""
    날짜 : 2020/06/22
    이름 : 오세훈
    내용 : 집합 자료형 실습하기 교재 p97
"""

# 집합 생성하기
set1 = set([1, 2, 3, 4, 5])
set2 = set([4, 5, 6, 7, 8])

# 집합 출력하기 - 리스트, 튜플로 변환 후 출력
ls = list(set1)
tp = tuple(set2)

print('set1: ', set1)
print('set2: ', set2)

print('ls: ', ls)
print('tp: ', tp)

# 교집합
print('set1과 set2의 교집합: ', set1 & set2)

# 합집합
print('set1과 set2의 합집합: ', set1 | set2)

# 차집합
print('set1과 set2의 차집합: ', set1 - set2)