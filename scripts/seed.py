import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from gradebook import service, storage

def seed():
    """
    Creates sample students, courses, enrollments, and grades.
    """
    print("Seeding database...")
    
    data = {
        "students": [],
        "courses": [],
        "enrollments": []
    }

    s1 = service.add_student(data, "Alice Smith")
    s2 = service.add_student(data, "Bob Jones")
    s3 = service.add_student(data, "Charlie Brown")

    service.add_course(data, "CS101", "Introduction to Computer Science")
    service.add_course(data, "PY201", "Advanced Python Programming")

    service.enroll(data, s1, "CS101")
    service.enroll(data, s1, "PY201")
    
    service.enroll(data, s2, "CS101")

    service.add_grade(data, s1, "CS101", 95.0)
    service.add_grade(data, s1, "CS101", 88.5)
    service.add_grade(data, s1, "PY201", 92.0)
    
    service.add_grade(data, s2, "CS101", 78.0)
    service.add_grade(data, s2, "CS101", 82.0)

    storage.save_data(data)
    
    print("Successfully seeded data/gradebook.json with:")
    print(f"- {len(data['students'])} Students")
    print(f"- {len(data['courses'])} Courses")
    print(f"- {len(data['enrollments'])} Enrollments")

if __name__ == "__main__":
    seed()