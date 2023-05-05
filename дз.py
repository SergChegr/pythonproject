import random
class animals:
    def __init__(self, name):
        self.name = name
        self.joy = 50
        self.progress = 0
        self.alive = True

    def to_study(self):
        print("Time to do something")
        self.progress += 0.12
        self.joy -= 3


    def to_sleep(self):
        print("I will sleep")
        self.joy += 3

    def to_chill(self):
        print("Rest time")
        self.joy += 5
        self.progress -= 0.1

    def is_alive(self):
        if self.progress < -0.5:
            print("I'm lazy…")
            self.alive = False
        elif self.joy <= 0:
            print("Not today…")
            self.alive = False
        elif self.progress > 5:
            print("Passed externally…")
            self.alive = False

    def end_of_day(self):
        print(f"joy = {self.joy}")
        print(f"Progress = {round(self.progress, 2)}")

    def live(self, day):
        day = "Day " + str(day) + " of " + self.name + " life"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
        self.end_of_day()
        self.is_alive()

nick = animals(name="cat")
kate = animals(name="dog")
for day in range(365):
    if nick.alive == False:
        break
    nick.live(day)
    if kate.alive == False:
        break
    kate.live(day)
