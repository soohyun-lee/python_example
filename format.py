#시험 성적 줄 맞추기
scores = {'수학':100, '영어':90, '국어':5}
for subject, score in scores.items():
    print(subject, score)
#=======================포맷 형태
#줄 맞추기
    print(subject.ljust(8), str(score).rjust(4))
# ljust(8) > 8칸의 공간을 확보한 상태로 왼쪽 정렬
# rjust(4) > 4칸의 공간을 확보한 상태로 오른쪽 정렬

#숫자에 00채우기 (1,2,3 이 아닌 001 002 003)
for num in range(1,90):
    print('대기번호:' + str(num).zfill(3))
# 3크기만큼 공간을 확보하고 값을 넣는데, 값이 없는 부분은 0으로 채워라

#빈자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print("{0: >10}".format(500))
#양수일 때는 +, 음수일 땐 -로 표시
print("{0: >+10}".format(500))
#왼쪽 정렬하고, 빈칸을 _로 채움
print("{0:_>+10}".format(500))
#3자리마다 콤마
print("{0:,}".format(10000000))
print(f"{1000000:,}원")
#3자미라 마다 콤마, 부호 붙이고, 30자릿수 확보하기, 빈자리는 ^로 채우기
print('{0:^<+30,}'.format(1000000000))