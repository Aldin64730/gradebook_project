class Student:
    def __init__(self,id,name):
        if not name.strip():
            raise ValueError("Student name cannot be empty")
        self.id = id
        self.name = name
    
    def __str__(self):
        return f"Student {self.name} with id {self.id}"


class Course:
    def __init__(self,code,title):
        self.code = code
        self.title = title
    def __str__(self):
        return f"Course:{self.title}, Code:{self.code}"

class Enrollment:
    def __init__(self,student_id,course_code,grades:list):
        self.student_id = student_id
        self.course_code = course_code
        self.grades = grades if grades is not None else []

        for g in self.grades:
            if not (0<=g<=100):
                raise ValueError("Grades must be between 0 and 100")

    def __str__(self):
        return f"Enrollment: Student {self.student_id} in {self.course_code}"