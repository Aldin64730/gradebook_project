import logging
from .models import Student, Course, Enrollment 

def add_student(data, name):
    """
    Validates a student using the Student model and adds it to data.
    """
    new_id = len(data["students"]) + 1
    student_obj = Student(new_id, name)
    
    student_dict = {"id": student_obj.id, "name": student_obj.name}
    data["students"].append(student_dict)
    logging.info(f"Added student: {name} with ID {new_id} [cite: 10]")
    return new_id

def add_course(data, code, title):
    """
    Validates a course using the Course model and adds it to data.
    """
    course_obj = Course(code, title)
    
    course_dict = {"code": course_obj.code, "title": course_obj.title}
    data["courses"].append(course_dict)
    logging.info(f"Added course: {title} with code {code} [cite: 10]")

def enroll(data, student_id, course_code):
    """
    Creates an enrollment using the Enrollment model.
    """
    enroll_obj = Enrollment(int(student_id), course_code, [])
    
    enroll_dict = {
        "student_id": enroll_obj.student_id,
        "course_code": enroll_obj.course_code,
        "grades": enroll_obj.grades
    }
    data["enrollments"].append(enroll_dict)
    logging.info(f"Enrolled student {student_id} in {course_code} [cite: 10]")

def add_grade(data, student_id, course_code, grade):
    """
    Adds a grade after validating it through the Enrollment model.
    """
    target = [e for e in data["enrollments"]
              if e["student_id"] == int(student_id) and e["course_code"] == course_code]
    
    if not target:
        raise ValueError(f"No enrollment found for student {student_id} in {course_code}")
    
    current_grades = target[0]["grades"] + [float(grade)]
    Enrollment(int(student_id), course_code, current_grades) 
    
    target[0]["grades"].append(float(grade))
    logging.info(f"Added grade {grade} for student {student_id} in {course_code} [cite: 10]")

def list_students(data, sort_by="name"):
    """Returns students sorted by name or id using lambda. [cite: 7, 8]"""
    return sorted(data["students"], key=lambda x: x[sort_by])

def compute_average(data, student_id, course_code):
    """Computes the mean grade for a specific course. """
    target = [e for e in data["enrollments"]
              if e["student_id"] == int(student_id) and e["course_code"] == course_code]
    
    if not target or not target[0]["grades"]:
        return 0.0
    
    grades = target[0]["grades"]
    return sum(grades) / len(grades)

def compute_gpa(data, student_id):
    """Computes the mean of all course averages for a student. """
    student_enrolls = [e for e in data["enrollments"] if e["student_id"] == int(student_id)]
    
    if not student_enrolls:
        return 0.0
    
    averages = [sum(e["grades"])/len(e["grades"]) for e in student_enrolls if e["grades"]]
    
    return sum(averages) / len(averages) if averages else 0.0