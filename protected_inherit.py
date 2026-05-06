class Parent:
    def __init__(self):
        self._age = 20   # protected

class Child(Parent):
    def show(self):
        print(self._age)  # accessible in child

obj = Child()
obj.show()

print(obj._age)  # possible but not recommended