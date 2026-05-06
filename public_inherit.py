class Parent:
    def __init__(self):
        self.name = "Sandeep"   # public

class Child(Parent):
    def show(self):
        print(self.name)  # accessible

obj = Child()
print(obj.name)  # accessible outside
obj.show()