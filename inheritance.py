class Mammal:
    def walk(self):
        print("walk")
        

class Dog(Mammal):
    def bark(self):
        print('Bark')
        

class Cat(Mammal):
    def meows(self):
        print('mianus')


cat1 = Cat()

cat1.meows()
cat1.walk()


dog1 = Dog()
dog1.walk()
dog1.bark()