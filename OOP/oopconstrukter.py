# ##########constucter########
#
#
#
# class Car:
#     def __init__(self, model, marka, color ):
#
#         self.model = model
#         self.marka = marka
#         self.color = color
#     #metod
#     def start(self):
#         print(f"{self.model} {self.marka}is starting")
#     def move(self):
#         print(f"{self.model} {self.marka}is moving")
#     def stop(self):
#         print(f"{self.model} {self.model}is stoping")
#
#     def full_up(self):
#         print(f"{self.model} {self.marka}is petrol")
#
#     def awaria(self):
#         print(f"{self.model} {self.marka} is avariaaa")
# mers = Car("mers","124","write")
# BMW = Car("BMW", "e60","black")
# mers.start()
# BMW.start()
# mers.full_up()
# BMW.awaria()


class Animals:
    def __init__(self,name,years,weight,paul):
        self.name = name
        self.years = years
        self.weight = weight
        self.paul = paul

# class Animals:
#     def __init__(self,name,years,weight,paul):
#         self.name = name
#         self.years = years
#         self.weight = weight
#         self.paul = paul
#
#     def became(self):
#         print(f"{self.name}  толко что проснулся от сна")
#     def hewants(self):
#         print(f"{self.name}  идет пить воду после жеcткого похмели унего жестко болиит голова")
#     def wantstoeat(self):
#         def obed(self,type):
#             print(f"{self.name}  хорошо похавал всей всей смейой {type} и пошли спат.КОНЕЦ")
#
#
#     lion=Animals("Лев","15","190кг","мужской")
#
#     lion.became()
#     lion.hewants()
#     lion.wantstoeat()
#     lion.eat("антилопу")
#     lion.obed("антилопа")
#         print(f"{self.name}  жестко голоден и хочет кушат он вышел искат добычу")
#     def eat(self,class Animals:
#     def __init__(self,name,years,weight,paul):
#         self.name = name
#         self.years = years
#         self.weight = weight
#         self.paul =



    #
    # lion.became()
    # lion.hewants()
    # lion.wantstoeat()
    # lion.eat("антило")

#
# class phone:
#     def __init__(self,model,marka,color,sena):
#         self.model = model
#         self.marka = marka
#         self.color = color
#         self.sena = sena
#
#     def modelss(self):
#         print(f"{self.model} {self.marka} вышло на продожу")
#     def markaaa(self):
#         print(f"Я купил {self.model} {self.marka} {self.color} {self.sena}")
#     def colorss(self):
#         print(f"Я проснулса от сна")
#
#
# iPhone = phone("iPhone","20 pro","мокрый асфалть за","150000")
# samsung = phone("SAMSUHG Galahy","A51","белый за","25000")
# iPhone.modelss()
# iPhone.markaaa()
# iPhone.colorss()
# samsung.modelss()
# samsung.markaaa()
# samsung.colorss()


# class Woman:
#     def __init__(self,name,where,year,lubimydela):
#         self.name = name
#         self.where = where
#         self.yaer = year
#         self.hoho = lubimydela

#     def oneday(self):
#         print(f"Ее зовут {self.name} она из {self.where} ей {self.yaer} она любит{self.lubimdela}")
#     def markaaa(self):
#         print(f"Мы каждый день перписаваемся через инстаграм")
#
#
#
# gerlfriend = Woman("Medina","Кара-Балты","18","она любит смотрет ужастики аниме любит слушать музыку прям как я и т.д")
#
# gerlfriend.oneday()
# gerlfriend.markaaa()

"""getter (алуу),  setter(кошуу кою),
__model(жабык),model public(ачык),
_model prodected(корголгон)
метод проглатывание"""
#
# class Compucter:
    # def __init__(self,model,marka,year,color,sena):
    #     self.__model = model
    #     self.__marka = marka
    #     self.__year = year
    #     self.__color = color
    #     self.__sena = sena
    #
    # def chykty(self):
    #     print(f"{self.__model}, {self.__marka} сатыка чыкты")
#     def kupil(self):
#         print(f"Мен {self.__model},{self.__marka},{self.__year},"
#               f"{self.__color},{self.__sena}мин сомго сатып алдым")
#
# # accer = Compucter("ACER","Windows 12","2023","матывый",
# #                   "56000 ")
# # accer.chykty()
# # accer.kupil()
#
# #########oop(мурастоо)(наследование)################
#
#
# class Animal:
#     def __init__(self,color,weight,food):
#         self.color = color
#         self.weight = weight
#         self.food = food
#
#     def move(self):
#         print(f"{self.name} is moving!!!")
#
#
#     def age(self):
#         print("Animal is eating!!!")
#
#     def drink(self):
#         print(f"{self.name} is driking!!!")
#
#
#
#
# class Dog(Animal):
#     def __init__(self,color,weight,food,name,age):
#         super().__init__(color,weight,food)
#         self.name = name
#         self.age = age
#
#     def voice(self):
#         print("Gaf-Gaf")
#
# tuzik = Dog("Black","20","Meat","Tuzik","age")
# tuzik.move()
# tuzik.voice()
# tuzik.drink()
#
#
# class Cat(Animal):
#     def __init__(self,color,weight,food,name,age):
#         super().__init__(color,weight,food)
#
#         self.name = name
#         self.age = age
#
#
#     def voice(self):
#         print("Miyau-Miyau")
#
#     def darak(self):
#         print(f"{self.name} daraka chuk")
#
#
# murka = Cat("write","3","milk","Murka","1")
#
# murka.move()
# murka.voice()
# murka.darak()


# class Human:
#     def __init__(self,name,jobtitle,year):
#         self.__name = name
#         self.__jobtitle = jobtitle
#         self.__year = year
#
#
#     def kodink(self):
#         print(f"{self.__name} кушает ")
#
#     def ahaha(self):
#         print(f"{self.__name} лежит ")
#
#     def hoohoh(self):
#         print(f"{self.__name} думает")
#
#
# class Teacher(Human):
#     def __init__(self,name,jobtitle,year,codic,partfeel):
#         super().__init__(name,jobtitle,year)
#         self.__codic = codic
#         self.__partfeel = partfeel
#
#
#     def voice(self):
#         print("Cалам")
#
#     def sabak(self):
#         print("Cабак отуп жатат")
#
# mahmud = Teacher("codic","teacher","35","уже 5 лет","haha")
#
# mahmud.voice()
# mahmud.sabak()
#
# class Conshik(Human):
#     def __init__(self,name,jobtitle,year,coonit,harosho):
#         super().__init__(name,jobtitle,year)
#
#         self.__coonit = coonit
#         self.__harosho = harosho
#
#
#
#     def gonit(self):
#         print(f" гооонит машину")
#
#     def horosho(self):
#         print(f" советует")
#
# ruslan = Conshik("Руслан","водитель машины","40","на 180","hoho")
#
# ruslan.gonit()
# ruslan.horosho()
#
#





###########  полиморфизим  #############

# def add(a: int , b: int):
#     return a + b
#
# def add(a: str, b: str):
#     return f" {a} {b}"
# def add(a: float, b:  float):
#     return round(a + b, 3)
#
# if __name__ == '__main__':
#     add(1,1)
# #
#
#
#
# class Animal:
#     def make_voice(self):
#         print("Animal is voice ")
#
# class Cat(Animal):
#     def make_voice(self):
#         print("meow")
#
# class Dog(Animal):
#     def make_voice(self):
#         print("Gaf-Gaf")
#
# def voice(animal:Animal):
#     animal.make_voice()
#
# if __name__ =="__main__":
#     voice(Cat())



# from abc import ABC , abstractmethod
# import math
#
# # базовой класс shape (фигура)
#
# class Shape(ABC):
#     @ abstractmethod
#     def calculeta_area(self):
#         pass
#
# class Rectangle(Shape):
#     def __init__(self,length,width):
#         self.length = length
#         self.width = width
#
#     def calculeta_area(self):
#         return self.length * self.width
#
# class Circle(Shape):
#     def __init__(self,radius):
#         self.radius = radius
#
#     def calculeta_area(self):
#         return math.pi * self.radius ** 2
#
#
# rectangle = Rectangle(4,5)
# circle = Circle(3)
# print("Плошадь прямоуголник:", rectangle.calculeta_area())
# print("Плошад круга:",circle.calculeta_area())
#
# from  abc import ABC, abstractmethod
# import math
#
# class Yehicle(ABC):
#     @abstractmethod
#     def drive(self):
#         pass
#
# class Car(Yehicle):
#
#
#     def drive(self):
#         return "едет на трасе"
#
# class Lodka(Yehicle):
#
#     def drive(self):
#     def drive(self):
#         return "едет по воде "
#
# class Velik(Yehicle):
#
#
#     def drive(self):
#         return "едет по велосипедной дорожке"
#
#
# car = Car()
# lodka = Lodka()
# velik = Velik()
#
# print("машина ",car.drive())
# print("лодка",lodka.drive())
# print("велосипед",velik.drive())


