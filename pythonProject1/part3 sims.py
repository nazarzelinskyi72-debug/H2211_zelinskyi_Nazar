import random

job_list = {
    "Java developer": {"salary": 50, "gladness_less": 10},
    "Python developer": {"salary": 40, "gladness_less": 3},
    "C++ developer": {"salary": 45, "gladness_less": 25},
    "Rust developer": {"salary": 70, "gladness_less": 1}

}

brands_of_car = {
    "BMW": {"fule": 100, "strength": 100 , "consumption": 12},
    "Lada": {"fule": 50, "strength": 40 , "consumption": 10},
    "Volvo": {"fule": 70, "strength": 150 , "consumption": 8},
    "Lexus": {"fule": 80, "strength": 120 , "consumption": 14}

}

class Human:

    def __init__(self, name="Human" , car=None,  home=None, job=None):


        self.name = name
        self.money = 100
        self.gladnes = 50
        self.satiety = 50
        self.job = job
        self.car = car
        self.home = home

    def get_home(self):
        self.home = Home()


    def get_car(self):
        self.car = Auto(brands_of_car)



    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = job(job_list)


    def eat(self):
        if self.home.food <= 0:
            self.shopping("food")
        else:
            if self.satiety >= 100:
                self.satiety = 100
                return
            self.satiety += 5
            self.home.food -= 5



    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fule < 20:
                self.shopping("fuel")
                return
            else:
                self.to_repair()
                return
        self.money += self.job.salary
        self.gladnes -= self.job.gladness_less
        self.satiety -= 4


    def shopping(self, manage):
        if self.car.drive():
            pass
        else:
            if self.car.fule < 20:
                self.shopping("fuel")
                return
            else:
                self.to_repair()
                return
        if manage == "fule":
            print("I bought fule")
            self.money -= 100
            self.car.fule += 100
        elif manage == "food":
             self.money -= 50
             self.home.food += 50
        elif manage == "delicacies":
            print("Hooray! Delicacies!")
            self.gladnes += 10
            self.satiety += 2
            self.money -= 15



    def chill(self):
        self.gladnes += 10
        self.home.mess += 5


    def clean_home(self):
        self.gladnes -= 5
        self.home.mess = 0

    def to_repair(self):
        self.car.strength += 100
        self.money -= 50


    def days_indexes(self, dey):
        dey  = f"Today the {day} of {self.name}'s light"
        print(f"{dey:=^50}", " \n")
        human_indexes = self.name+"'s indexes"
        print(f"{human_indexes:-^50}","/n")
        print(f"Money- {self.money}")
        print(f"satiety - {self.satiety}")
        print(f"Gladness - {self.gladnes}")
        home_indexes = "Home indexes"
        print(f"{home_indexes:-^50}", "/n")
        print(f"food - {self.home.food}")
        print(f"Mess - {self.home.mess}")
        car_indexes = f"{self.car.brend}  car indexes"
        print(f"{car_indexes:-^50}", "/n")
        print(f"Fuel - {self.car.fule}")
        print(f"Strength - {self.car.strength}")

    def is_alive(self):
        if self.gladnes < 0:
            print("Depression...")
            print("Gayyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy")
            return False
        if self.satiety <0:
            print("Dead...")
            return False
        if self.money < -500:
            print("Bankrut")
            return False
    def live(self, day):
        if self.is_alive() == False:
            return False
        if self.home is None:
            self.get_home()
        if self.car is None:
            self.get_car()
            print(f" I bought a car {self.car.brend}")
        if self.job is None:
            self.get_job()
            print(f"I get a job {self.job.job}  with salary {self.job.salary}  ")
            self.days_indexes(day)
            dice = random.randint(1, 4)
            if self.satiety < 20:
                print("I'll go eat")
                self.eat()
            elif self.gladnes < 20:
                if self.home.mess > 15:
                    print("I will clean the house")
                    self.clean_home()
                else:
                    print("let's chill!")
                    self.chill()
            elif self.money < 0:
                print("Start working")
                self.work()
            elif self.car.strength < 15:
                print("I repair my car")
                self.to_repair()
            elif dice == 1:
                self.chill()
            elif dice == 2:
                self.work()
            elif dice == 3:
                self.clean_home()
            elif dice == 4:
                self.shopping(manage ="delicacies")








class Auto:
    def __init__(self, brand_list):
        self.brend = random.choice(list(brand_list))
        self.fuel = brand_list[self.brend]["fule"]
        self.strength = brand_list[self.brend]["strength"]
        self.consumption = brand_list[self.brend]["consumption"]

    def drive(self):
        if self.strength >0 and self.fuel > self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print("the car cannot move")
            return  False
class Home:
    def __init__(self):
        self.mess = 0
        self.food = 0

class job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]["salary"]
        self.gladness_less = job_list[self.job]["gladness_less"]


persona = Human(name="Vasya")
for day in range(1, 8):
    if persona.live(day) == False:
        break


# print()



