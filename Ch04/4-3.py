"""
    날짜 : 2020/06/23
    이름 : 오세훈
    내용 : 파일 읽고 쓰기 교재 p171
"""

# 파일 읽기
file = open('C:/Users/bigdata/Desktop/test.txt')
line = file.readline()

print('line: ', line)
file.close()    # 파일 닫기

# 여러줄 파일 읽기
file = open('C:/Users/bigdata/Desktop/test.txt', 'r')

while True:
    line = file.read()

    if not line:     # 라인이 없으면
        break

    print('line: ', line)

file.close()

# 파일 쓰기
sample = open('C:/Users/bigdata/Desktop/sample.txt', 'w')
sample.write('안녕하세요.\n')
sample.write('반갑습니다.\n')
sample.write('감사합니다.\n')
sample.close()

# 구구단 파일 생성하기
gugudan = open('C:/Users/bigdata/Desktop/gugudan.txt', 'w')

for dan in range(2, 10):
    gugudan.write('%d단\n' % dan)
    for num in range(1, 10):
        gugudan.write('%d x %d = %d\n' % (dan, num, dan*num))

gugudan.close()

# with문을 이용한 파일 입출력
with open('C:/Users/bigdata/Desktop/star.txt', 'w') as star:
    for i in range(1, 11):
        star.write('☆'*i)
        star.write('\n')

