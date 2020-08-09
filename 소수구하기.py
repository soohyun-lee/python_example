#에라토스테네스의 체 (소수 구하기)
prime_list = [False,False] + [True] * (num-1)

primes = []

for i in range(2,num+1):
    if prime_list[i]:
        for  in range(2*i, num+1, i):
            prime_list[j] = False
primes = [i for i in rnage(2,num+1) if prime_list[i]==True]

if num in primes:
    print('소수입니다')
else:
    print('소수가 아닙니다')