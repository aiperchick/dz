# class SuperHero:
#     people = 'people'
#
#     def __init__(self, name, nickname, superpower, health_points, catchphrase):
#         self.name = name
#         self.nickname = nickname
#         self.superpower = superpower
#         self.health_points = health_points
#         self.catchphrase = catchphrase
#
#     def realname(self):
#          return f'{self.name}'
#     def hpx2(self):
#         return f'{self.health_points * 2}'
#     def __str__(self):
#         return  f'{self.nickname, self.superpower, self.health_points}'
#     def __int__(self):
#         return len(self.catchphrase)
# Hero=SuperHero('Ben', 'Batman','деньги',200,'все хотят от меня шоу')
# Hero.realname()
# Hero.hpx2()
#
# print(Hero.realname())
# print(Hero.hpx2())
#
# class Earth(SuperHero):
#     sign = True
#     def __init__(self,name,nickname,superpower,health_points,catchphrase,damage=False,fly=False):
#         super().__init__(name,nickname,superpower,health_points,catchphrase)
#         self.damage = damage
#         self.fly = fly
#     def hpx2(self):
#         return f'{self.health_points ** 2}'
#     def fly_h(self):
#         self.fly=True
#
#     def phrase(self):
#         print('fly in the True_phrase')
#
#
# Earth_h = Earth('Bob', 'Stebel', 'laser', 100, 'babushka boi')
# Earth_h.hpx2()
# Earth_h.phrase()
# print(Earth_h.hpx2())
#
#
# class Air(SuperHero):
#     cape = True
#     def __init__(self,name,nickname,superpower,health_points,catchphrase,damage=False,fly=False):
#         SuperHero.__init__(self,name,nickname,superpower,health_points,catchphrase)
#         self.damage = damage
#         self.fly = fly
#     def hpx2(self):
#         return  f'{self.health_points **2}'
#     def fly_h(self):
#         self.fly=True
#
#     def phrase(self):
#          print('fly in the True_phrase')
#
# Air_h = Air('carl','invisy', 'invisible', 30, 'where am i')
# Air_h.hpx2()
# Air_h.phrase()
# print(Air_h.hpx2())
#
#
# class Villain(Air):
#     people = 'monster'
#     def __init__(self,name,nickname,superpower,health_points,catchphrase,damage=False,fly=False):
#         super().__init__(name,nickname,superpower,health_points,catchphrase,damage=False,fly=False)
#     def gen_x(self):...
#     def crit(self):
#         print(f'{self ** 2}')
# evil = Villain('Ivan','kuvalda','strength',300,'я бью 2 раза')
# Villain.crit(Air_h.damage)


class Bank:

    def __init__(self, name, balanse):
        self._name = name
        self._balanse = balanse

    def __str__(self):
        return (f'name: {self._name}\n'
                f'balance: {self._balanse}')

    def moneyX(self):
        cash = int(input('пополнить текущий баланс на: '))
        self._balanse += cash

    def _kill(self):
        self._balanse *= 0

    def __jackpot(self):
        self._balanse *= 10

    def _second(self):
        user2._balanse += user._balanse
        print(f'баланс бекболота: {user2._balanse}\n'
              f'баланс айпери: {user._balanse}')


user = Bank('aiperi', 45)
user2 = Bank('bekbolot', 30)
# user.moneyX()
# user._kill()
# user._Bank__jackpot()
# print(user._balanse)
user._second()
















