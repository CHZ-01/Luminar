class Student:
    def __init__(self, name_of_student, physics_mark, chemistry_mark, maths_mark):
        self.name_of_student = name_of_student
        self.physics_mark = physics_mark
        self.chemistry_mark = chemistry_mark
        self.maths_mark = maths_mark
    
    def average_mark(self):
        average_mark = self.physics_mark + self.chemistry_mark + self.maths_mark /3
        print("Average Mark:",average_mark)

    def max_mark_subject(self):
        if self.physics_mark == self.chemistry_mark and self.physics_mark > self.maths_mark:
            print("Both Physics and Chemistry marks are highest:",self.physics_mark)
        elif self.physics_mark == self.maths_mark and self.physics_mark > self.chemistry_mark:
            print("Both Physics and Maths marks are highest:",self.physics_mark)
        elif self.chemistry_mark == self.maths_mark and self.chemistry_mark > self.physics_mark:
            print("Both Chemistry and Maths marks are highest:",self.chemistry_mark)
        elif self.physics_mark > self.chemistry_mark and self.physics_mark > self.maths_mark:
            print("Physics has the highest mark:",self.physics_mark)
        elif self.chemistry_mark > self.physics_mark and self.chemistry_mark > self.maths_mark:
            print("Chemistry has the highest mark:",self.chemistry_mark)
        else:
            print("Maths has the highest mark:",self.maths_mark)

student1 = Student("Vaisakh", 90, 88, 97)
student1.average_mark()
student1.max_mark_subject()