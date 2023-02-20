import Student
import Grades

p1=Student.Student("Espiritu, Marcus Joshua D.C.", 25)
p1Grades=Grades.Grades("CPE028", 3, 1)
print(p1)

print ("Name:", p1.name)
print ("Age:",p1.age)
print ("Course Code:",p1Grades.Course_Code)
print ("Course Units:",p1Grades.Course_Units)
print ("Course Grades:",p1Grades.Course_Grade)