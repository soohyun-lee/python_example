# 사용자 정의 예외처리
try:
    print('나누기 전용 계산기')
    num1 = int(input('첫번째 숫자를 입력하세요'))
    num2 = int(input('두번째 숫자를 입력하세요'))
    print('{} / {} = {}'.format(num1, num2, int(num1 / num2)))
except ValueError:
    print('에러가 발생')
except ZeroDivisionError as err:  # as로 에러 내용 받기
    print(err)
# 위의 에러 외에 나머지 에러 일 경우
except Exception as err:
print(err)
 # 추가하기! as err 를 통해 에러 내용 전달

# 에러 발생 시키기
try:
    print('한자리 숫자 나누기 전용 계산기')
    num1 = int(input('첫 번째 숫자 입력:'))
    num2 = int(input('두 번째 숫자 입력:'))
    if num1 >= 10 or num2 >= 10:
        raise ValueError
    print('{} / {} = {}'.format(num1, num2, int(num1 / num2)))
except ValueError:
    print('잘못된 값을 입력하였습니다. 한자리 숫자만 입력하세요')


# 에러 발생 시키기2
class BigNumberError(Exception):
    pass
try:
    print('한자리 숫자 나누기 전용 계산기')
    num1 = int(input('첫 번째 숫자 입력:'))
    num2 = int(input('두 번째 숫자 입력:'))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError
    print('{} / {} = {}'.format(num1, num2, int(num1 / num2)))
except ValueError:
    print('잘못된 값을 입력하였습니다. 한자리 숫자만 입력하세요')
except BigNumberError:
    print('에러가 발생했습니다다')

# finally > 정상이든 오류든 무조건 실행시키는 문구
class BigNumberError(Exception):
    pass
try:
    print('한자리 숫자 나누기 전용 계산기')
    num1 = int(input('첫 번째 숫자 입력:'))
    num2 = int(input('두 번째 숫자 입력:'))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError
    print('{} / {} = {}'.format(num1, num2, int(num1 / num2)))
except BigNumberError:
    print('에러가 발생했습니다다')
finally:
    print('계산기를 이용해주셔서 감사합니다')

# 에러가 발생했습니다. 계산기를 이용해주셔서 감사합니다.

# 치킨 주문 시스템 예제
class soldOutError(Exception):
    pass

chicken = 10
waiting = 1
while True:
    try:
        print('남은 치킨 {}'.format(chicken))
        order = int(input('치킨 몇마리:'))
        if order > chicken:
            print('재료가 부족합니다')
        elif order < 1 or order == str:
            raise ValueError
        else:
            print('대기번호 {}, {}마리 주문 완료 됨'.format(waiting, order))
            waiting += 1
            chicken -= order
        if chicken == 0:
            raise soldOutError
    except ValueError:
        print('잘못된 값을 입력했습니다.')
    except soldOutError:
        print('재료가 소진되어 더 이상 주문 안받아요')
        break
