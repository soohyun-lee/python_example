# 자릿수의 합 구하기
# N개의 숫자 중, 각 자리수의 합 더해서 가장 큰 수 찾기 (EX, 123 => 6, 97 -> 16 >>> 그럼 97 찾기)
# ver1 (몫과 나머지로 구하기)
n = int(input('몇 개?:'))
a = list(map(int,input('n개의 숫자 리스트 입력').split()))
def digit_sum(x):
    sum=0
    while x > 0:
        sum += x%10
        x = x //10
    return sum

max =- 2147000000
for x in a:
    tot = digit_sum(x)
    if tot > max:
        max = tot
        res = x
print(res)

#ver2 (str으로 구하기)
n = int(input('몇 개?:'))
a = list(map(int,input('n개의 숫자 리스트 입력').split()))
def digit_sum(x):
    sum=0
    for i in str(x):
        sum += int(i)
    return sum

max =- 2147000000
for x in a:
    tot = digit_sum(x)
    if tot > max:
        max = tot
        res = x
print(res)

# 뒤집은 숫자 중 소수인 숫자 찾기
def reverse(x):
    res = 0
    while x > 0:
        t=x%10
        res = res*10 + t
        x = x//10
    return res
def isPrime(x):
    if x == 1:
        return False
    for i in range(2,x//2+1):
        if x%i == 0:
            return False
    else:
        return True

n = int(input('몇 개?:'))
a = list(map(int,input('n개의 숫자입력').split()))
for x in a:
    tmp=reverse(x)
    if isPrime(tmp):
        print(tmp,end=',')