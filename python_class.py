class Person:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print('안녕하세요. 나는 ' + self.name)


soohyun = Person('수현')
michael = Person('마이클')
jaehyun = Person('재현')

soohyun.say_hello()
michael.say_hello()
jaehyun.say_hello()


class Person:
    def __init__(self, name):
        self.name = name

    def say_hello(self, to_name):
        print('안녕하세요' + to_name + '나는' + self.name)


soohyun = Person('수현')
michael = Person('마이클')
jaehyun = Person('재현')

soohyun.say_hello('철수')
michael.say_hello('철수')
jaehyun.say_hello('철수')