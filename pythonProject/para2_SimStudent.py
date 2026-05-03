import random


class Student:

    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progres = 0
        self.alive = True

    def to_study(self):
        print("Time to study")
        self.progres += 0.12
        self.gladness -= 5

    def to_sleep(self):
        print("I will sleep")
        self.gladness += 5

    def to_chill(self):
        print("Rest time")
        self.gladness += 5
        self.progres -= 0.1


    def is_alive(self):
        if self.progres < -0.5:
            print("Cast out...")
            self.alive = False
        elif self.gladness < 0:
            print("Depression")
            self.alive = False
        elif self.progres > 5:
            print("passed externally...")
            self.alive = False

    def end_of_day(self):
        print(f"gladness = {self.gladness}")
        print(f"Progress = {self.progres}")

    def live(self, day):
        day = f"Day {day} of {self.name} life"
        print(f"{day:=^50}")
        live_cube = random.randint(1,3)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
        self.end_of_day()
        self.is_alive()


personage = Student(name="Vasya")

for day in range(365):
    if personage.alive == False:
        break
    personage.live(day)