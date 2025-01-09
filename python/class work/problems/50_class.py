class Student:
    school_name = "Luminar"
    
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark

    def display(self):
        print("School Name:", self.school_name)
        print("Student Name:", self.name)
        print("Mark:", self.mark)

    def grade_check(self):
        if self.mark >= 90 and self.mark <= 100:
            print("Grade: A") 
        elif self.mark >= 80 and self.mark < 90:
            print("Grade: B") 
        elif self.mark >= 70 and self.mark < 80:
            print("Grade: C") 
        elif self.mark >= 60 and self.mark < 70:
            print("Grade: D") 
        else:
            print("Grade: F") 

std1 = Student("Vaisakh",100)
std1.display()
std1.grade_check()

std2 = Student("John",70)
std2.display()
std2.grade_check()