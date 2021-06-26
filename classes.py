class Point():
    def move(self):
        print('move')

    def draw(self):
        print('draw')


point1 = Point()

point1.move()
point1.draw()

point1.name = 'Olamide'
point1.hobbies = ['Reading', 'Coding', 'Programming']

print(point1.name)
print(point1.hobbies)

# Constructors
# Constructor is a function that get called at the time of creating an object

class ClassName(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

        super(ClassName, self).__init__()
        

className1 = ClassName(20, 30);

print(className1.x);
print(className1.y);

        