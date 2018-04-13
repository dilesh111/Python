# Instance Variable


class Enemy:

    def __init__(self, atkl, atkh):
        self.atkl = atkl
        self.atkh = atkh

    def getattack(self):
            print(self.atkl)

    def getattack1(self):
            print(self.atkh)


enemy1 = Enemy(30, 50)
enemy1.getattack()

enemy2 = Enemy(70, 90)
enemy2.getattack1()
'''
