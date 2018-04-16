'''
newfile = ("newfile1.txt", "w+")
string = "This is the content that will written to th text file"
newfile.write(string)

'''

# Instance Variable


class Enemy:

    def __init__(self, atkl, atkh):
        self.atkl = atkl
        self.atkh = atkh

    def getattack(self):
            print(self.atkl)

    def getattack1(self):
            print(self.atkh)
