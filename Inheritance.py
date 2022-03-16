#  20CE098, Pranay Patel
#  Practical 8
#  Consider an example of declaring the examination result. Design three classes: Student, Exam, and Result.
#  The Student class has data members such as those representing rollNumber, Name, etc. Create the class Exam by
#  inheriting Student class. The Exam class adds fields representing the marks scored in six subjects. Derive Result
#  from the Exam class, and it has its own fields such as total_marks. Write an interactive program to model this
#  relationship.
class Student:
    def __init__(self, name, num):
        self.rollno = num
        self.name = name
    
class Exam(Student):
    def __init__(self,name,num,marks):
        Student.__init__(self,name,num)
        self._marks = marks

class Result(Exam):
    def __init__(self,name,num,marks):
        Exam.__init__(self,name,num,marks)
        self.total_marks = sum(marks)
        self.percentage = (self.total_marks/150)*100
    def display(self):
        print(f"Name: {self.name}, RollNo: {self.rollno}, Total marks: {self.total_marks}, Percent: {self.percentage}%")
    
       
if __name__ == '__main__':
    s1 = Result('Smit', 1, [45, 40, 45])
    s2 = Result('Dev', 2, [37, 37, 40])
    s3 = Result('Soni', 3, [30, 15, 50])
    s4 = Result('Jay', 4, [45, 35, 25])

    s1.display()
    s2.display()
    s3.display()
    s4.display()
