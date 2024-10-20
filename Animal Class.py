from abc import ABC,abstractmethod
class Animal(ABC):
    def move(self):
        pass
    
class Human(Animal):
    def move(self):
        print("I can walk and run")
        
class Snake(Animal):
    def move(self):
        print("I can crawl")
        
class Dog(Animal):
    def move(self):
        print("I can bark")
        
class Lion(Animal):
    def move(self):
        print("I can roar")
        
r = Human()
r.move()
r1 = Snake()
r1.move()
r2 = Dog()
r2.move()
r3 = Lion()
r3.move()