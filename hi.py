from random import randint

my_sum = 0


class Student():
    my_sum = 0
    money = 0
    def __init__(self, name="tony", age=99, facescore=99, strence=99, yu=99, shu=99, wai=99, speed = None, direction = None):
        self.name = name
        self.age = age
        self.facescore = facescore
        self.shu = shu
    def play(self):
        self.speed = randint(70, 100)
        self.direction = randint(70, 100)
        print("your speed is " + str(self.speed) + " , and your direction is " + str(self.direction) + ".")
        pspeed = randint(70, 100)
        pdirection = randint(70, 100)
        print("your enemy's speed is " + str(pspeed) + ", and your enemy's direction is " + str(pdirection) + ".")
        if pspeed > self.speed:
            print("his speed is faster than yours!")
        if pspeed == self.speed:
            print("you two just like a brother !! you needn't a basketball game, just back to the home and***.")
        if pspeed < self.speed:
            print("his speed is slower than yours!")
            self.my_sum +=  1
        if pdirection > self.direction:
            print("his direction is better than yours!")
        if pdirection == self.direction:
            print("you two just like a brother !! you needn't a basketball game, just back to the home and***.")
        if pdirection < self.direction:
            print("his direction is worse than yours!")
            self.my_sum +=  1
        if self.my_sum == 1:
            print("tie!!")
        if self.my_sum > 1:
            print("you win!!!")
            self.money += 100
        if self.my_sum < 1:
            print("you lose hahahahahahahaha")
    
    def get_money(self):
        print("you have " + str(self.money) + " $")

    def attack(self, player):
        message = self.name + " attacked " + player.name
        player.shu = player.shu - 10
        print("{} only have {} health left".format(player.name, player.shu))

