def create_student(): #function
    class Student: #class
        def __init__(self, name, marks): #__init__ constructor and it initializes values to an object
            self.name=name
            self.marks=marks

        def show(self):
            print("Name:", self.name)
            print("Marks:", self.marks)

    s=Student("Rahul", 85)
    s.show()

create_student()