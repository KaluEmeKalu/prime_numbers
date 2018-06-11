from random import randint

my_sum = 0


class Student():
    my_sum = 0
    money = 0
    def __init__(self, name="tony", age=99, facescore=99, strence=99, yu=99, shu=100, wai=100, speed = None, direction = None):
        self.name = name
        self.age = age
        self.facescore = facescore
        self.shu = shu
        self.wai = wai
    def play(self):
        self.my_sum = 0
        if self.wai < 0:
            print("you are so tired! get to the bed!")
        else :
            self.speed = randint(10, 100)
            self.direction = randint(10, 100)
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
            self.wai -= 25
    
    def get_money(self):
        print("you have " + str(self.money) + " $")

    def attack(self, player):
        message = self.name + " attacked " + player.name
        player.shu = player.shu - 10
        print("{} only have {} health left".format(player.name, player.shu))

    def go_to_store(self):
        print("there are soap,  cola, book.")

    def get_soap(self):
        if self.money > 100:
                self.speed += 1000
                self.money -= 100
                print("you get a soap, it spend you 100$.now, your speed are faster!")
    def get_cola(self):
        if self.money > 100:
                self.direction += 1000
                self.money -= 100
                print("you get a cola, it spend you 100$.now, your direction are better!")

    def get_bed(self):
        print("you are sleeping!")
        print("ZZZZZ")
        print("ZZZZZ")
        print("ZZZZZ")
        print("ZZZZZ")
        print("ZZZZZ")
        print("ZZZZZ")
        print("ZZZZZ")
        print("ZZZZZ")
        print("ZZZZZ")
        print("ZZZZZ")
        print("ZZZZZ")
        print("ZZZZZ")
        self.wai += 50
        print("you are aweak")

tony = Student("Tony")