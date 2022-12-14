
class Сalkulator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        user1 = int(input(f'введите первое число: '))
        user2 = int(input(f'введите первое число: '))

    def __add__(self):
        return self.a + self.b

    def __sub__(self):
        return self.a - self.b

    def __mul__(self):
        return self.a * self.b

    def __truediv__(self):
        return self.a // self.b

a = int(input(f'введите первое число: '))
b = int(input(f'введите первое число: '))

calkulator = Сalkulator(a, b)

print('1 - сложение')
print('2 - вычитание')
print('3 - умножение')
print('4 - деление')
c = int(input('выберите оперцию: '))
if c == 1:
    print(calkulator.__add__())
elif c == 2:
    print(calkulator.__sub__())
elif c == 3:
    print(calkulator.__mul__())
elif c == 4:
    print(calkulator.__truediv__())
else:
    print('ошибка')

