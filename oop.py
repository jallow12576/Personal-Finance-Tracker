class Student:
    def __init__(self, name, age, grade, grade_level):
        self.name = name
        self.age = age
        self.grade = grade
        self.grade_level = grade_level
        self.courses = []

    def display_student(self):
        student = {
            'name': self.name,
            'age': self.age,
            'grade': self.grade,
            'grade_level': self.grade_level
        }
        return student
    
    def promote(self):
        try:
            current_grade = int(self.grade)
            new_grade = current_grade + 1
            return f'{self.name} is promoted to {new_grade} {self.grade_level}'
        except ValueError:
            return f'Error: Cannot promote {self.name} to {self.grade}'
    
    def add_courses(self, course_name):
        self.courses.append(course_name)
        return f'Course: {course_name} is added for {self.name}'
    
    def remove_course(self, course_name):
        self.courses.remove(course_name)
        return f'Course: {course_name} has been removed from the list for {self.name}'
    
    def print_courses(self):
        if not self.courses:
            print('There is no courses')
            return
        
        print(f'{self.name} enrolled courses:')
        for course in self.courses:
            print(f'-{course}')
        
        
        


student1 = Student('Yaya Jallow', 20, '11', 'commerce 2')
student2 = Student('Abubacarr Jaiteh', 20, '11', 'commerce 2')

print(student1.display_student())
print(student2.display_student())
print(student1.promote())
print(student1.add_courses("Python Course"))
print(student1.add_courses("Digital Marketing"))
print(student2.add_courses('Acounting'))
print(student2.add_courses('Finance'))
print(student2.add_courses('Economics'))
print('Courses for Yaya:')
student1.print_courses()

