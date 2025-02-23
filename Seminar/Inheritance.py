# Parent class
class school:
    def student(self):
        print("student")
    def teacher(self):
        print("teacher")
    def classes(self):
        print("classes")

# Child class
class names(school):
    def student_name(self):
        print("student_name")
    def teacher_name(self):
        print("teacher_name")
    def class_name(self):
        print("class_name")

# Creating an object of the child class
obj = names()

# Calling methods of the parent using the child class object
obj.student()
obj.teacher()
obj.classes()

print()

# Calling methods of the child class
obj.student_name()
obj.teacher_name()
obj.class_name()