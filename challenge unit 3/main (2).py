class Student:

 def__init__(self,name,roll_number,cgpa)
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa

def sort_students(student_list):
     sorted_students = sorted(student_list,
                              key=lambda student: student.cgpa,
                              reverse=True)

     return sorted_students



students =[Student("parthi","cb22s614308", 8.1),
            Student("raj","cb22s614394",8.5),
            Student("sakthi","cb22s614399",9.1),
            Student("sabari","cb22s614398",9.9)]

sorted_students = sort_students(students)

for  student in sorted_students:
     print("Name: {},Roll Number:{},CGPA:{}",format(students))
