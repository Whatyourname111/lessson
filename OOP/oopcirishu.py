################### OOP ###################
"""class , талаа , метод , обьект """
class Car:
    model = "BMW"
    marka = "e60"
    year = 2011
    color = "black"
    #metod
    def start(self):
        print("Car is srarting!!!")
    def move(self):
        print("Car is moving!!!")
    def stop(self):
        print("Car is stoping!!!")

bmw_e60 = Car()

bmw_e60.start()
bmw_e60.move()
bmw_e60.stop()