class Cat(object):
    """ Virtual Cat """
    total = 0
    @staticmethod
    def count():
        print("Total cats: ", Cat.total)
        
    def __init__(self):
        print("A new cat was born!")
        self.name = input("How will we name it? ")
        Cat.total += 1
        self.__w = 300
        self.hunger = 1
        
    def __str__(self):
        res = "Virtual Cat\n name: " + self.name + "\n Weight: " + str(self.__w)
        return res

    @property
    def weight(self):
        return self.__w

    def talk(self):
        print(self.name, ": Meow")
        
    def eat(self):
        if self.hunger == 5:
            print("The cat is not hungry")
        else:
            self.hunger += 1
            self.__w += 30
            print("Moore!")
            
    def play(self):
         self.talk()
         self.__w -= 5
         if self.hunger > 0:
             self.hunger -= 1
         else:
             self.hunger = 1

def main():
    
    bagira = Cat()
    choice = None  
    while choice != "0":
        print \
        ("""
        What do we do?
    
        0 - Exit
        1 - Talk
        2 - Feed
        3 - Play
        4 - Get weight
        """)
    
        choice = input(">>: ")
        print()

        # exit
        if choice == "0":
            print("Bye.")

        # мяукане
        elif choice == "1":
            bagira.talk()
        
        # хранене
        elif choice == "2":
            bagira.eat()
         
        # игра
        elif choice == "3":
            bagira.play()
        elif choice == "4":
            print("Weight: ", bagira.weight, " g.")

        # недопустими данни
        else:
            print("\nIncorrect choice!")

main()
