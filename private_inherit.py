class Parent:
    def __init__(self):
        self.__salary = 50000   # private

    def get_salary(self):
        return self.__salary


class Child(Parent):
    def show(self):
        # print(self.__salary)  ERROR
        print("Access via method:", self.get_salary())

obj = Child()
obj.show()

# print(obj.__salary) ERROR