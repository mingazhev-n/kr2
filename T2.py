import random


class Player:
    def __init__(self, name):
        self.name = name

    def hit(self):
        t = random.random()
        if t >= 0.8:
            return False
        else:
            return True


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def start(self):
        p11 = 0
        p21 = 0
        while p11 < 11 or p21 < 11:
            if p1.hit():
                p11 += 1
            else:
                p21 += 1

        if p11 == 11:
            return p1.name
        else:
            return p2.name


p1 = Player('Ping')
p2 = Player('Pong')
game = Game(p1, p2)
print(game.start())


print("-" * 200)
a = input("Введите текст").split()
q = ["w", "a", "z", "u", "p"]
for i in a:
    c = True
    if len(i) > 5:
        for i1 in q:
            if i1 not in i.lower():
                c = False
    else:
        continue
    if not c:
        continue
    print(i)




