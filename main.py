from abc import ABC,abstractmethod
class Animal(ABC):
    def move(self):
        pass
class Human(Animal):
    def move(self):
        print('Humans can walk & run')

class Dog(Animal):
    def move(self):
        print('Dogs can also walk & run')

class Snake(Animal):
    def move(self):
     print('Snakes can just crawl')

class Bird(Animal):
    def move(self):
        print('Birds can fly, walk and & run')

H1=Human()
H1.move()
D1=Dog()
D1.move()
S1=Snake()
S1.move()
B1=Bird()
B1.move()