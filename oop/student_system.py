class Student:
    next_id =1000
    def __init__(self,name,grade):
        (self,name,grade)
        self.name= name
        self.grade = grade
        self.student_id= Student.next_id
        # تخصیص id جدید و افزایش خودکار شمارنده
        Student.next_id +=1
        # دیکشنری برای ذخیره درس ونمرات
        self.grades = {}
    def add_grades (self,course_name,mark):
        if not isinstance(mark,(int,float)) or not ( 0<=mark<=20 ) :
            print (f"error! mark for course'{course_name}' must beetwin 0,20")
            return
        self.grades[course_name]= mark
        print(f'mark "{mark}" for course"{course_name}" for student"{self.name}" (ID:{self.student_id})added')
        #نمایش اطلاعات دانش آموزان به همراه نمرات
        def display_info(self):
            print (f"\n  name:{self.name}")
            print (f"\n student id:{self.student_id}")
            print (f"\n  grade :{self.grade}")
            print("marks")
            if self.grades :
                for course,score in self.grades.items():
                    print(f"-{course}:{score}")
            else :
                print("can not find")
                print('---------')
class School :
    def __init__(self,name):
        self.name = name
        #دیکشنری برای ذخیره دانش آموز با کد ID دانش آموز
        self.students= {}
    def add_student(self,name,grade):
      # شی از کلاس student    
      new_student = Student(name,grade) 
      self.students[new_student.student_id]=new_student
      print(f"student:'{new_student.name}'ID:'{new_student.student_id}'added to:'{self.name}'")
      return new_student
    def find_student (self,student_id):
        return self.students.get(student_id)
    def display_all_students(self):
        print(f"\n student list of:{self.name}:\n")
        if not self.students :
            prin(" List is empty")
            return
        sorted_ids = sorted(self.students.keys())
        # sid = student_id
        for sid in sorted_ids:
            self.students[sid].display_info()
     # ایجاد نمونه مدرسه       
my_school=School("Future School")
s1= my_school.add_student("ali ahmadi",10)             
s2= my_school.add_student("maryam rezaei",11)             
s3= my_school.add_student("reza karami",10) 
     # اضافه کردن نمرات
s1.add_grades("mathematic",19)
s1.add_grades("science",18) 
s2 .add_grades("chemistry",16)
s2.add_grades("letters",20)
s3.add_grades("geometry",15)
my_school.display_all_students    

      
         
       
                              