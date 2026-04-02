import argparse
import sys
import logging
from gradebook import storage, service
from gradebook.utils import parse_grade

def main():
    logging.basicConfig(
        filename='logs/app.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

    data = storage.load_data()
    
    parser = argparse.ArgumentParser(description="Gradebook CLI Application")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    parser_student = subparsers.add_parser("add-student", help="Add a new student")
    parser_student.add_argument("--name", required=True, help="Full name of student")

    parser_course = subparsers.add_parser("add-course", help="Add a new course")
    parser_course.add_argument("--code", required=True, help="Course code")
    parser_course.add_argument("--title", required=True, help="Course title")

    parser_enroll = subparsers.add_parser("enroll", help="Enroll student in course")
    parser_enroll.add_argument("--student-id", type=int, required=True)
    parser_enroll.add_argument("--course", required=True)

    parser_grade = subparsers.add_parser("add-grade", help="Add grade to enrollment")
    parser_grade.add_argument("--student-id", type=int, required=True)
    parser_grade.add_argument("--course", required=True)
    parser_grade.add_argument("--grade", type=float, required=True)

    parser_list = subparsers.add_parser("list", help="List data")
    parser_list.add_argument("type", choices=["students", "courses", "enrollments"])
    parser_list.add_argument("--sort", choices=["name", "code"], default="name")

    parser_avg = subparsers.add_parser("avg", help="Show course average")
    parser_avg.add_argument("--student-id", type=int, required=True)
    parser_avg.add_argument("--course", required=True)

    parser_gpa = subparsers.add_parser("gpa", help="Show student GPA")
    parser_gpa.add_argument("--student-id", type=int, required=True)

    args = parser.parse_args()

    try:
        if args.command == "add-student":
            new_id = service.add_student(data, args.name)
            print(f"Successfully added student '{args.name}' with ID: {new_id}")
        
        elif args.command == "add-course":
            service.add_course(data, args.code, args.title)
            print(f"Successfully added course: {args.code}")
        
        elif args.command == "enroll":
            service.enroll(data, args.student_id, args.course)
            print(f"Enrolled student {args.student_id} in {args.course}")
        
        elif args.command == "add-grade":
            validated_grade = parse_grade(args.grade)
            service.add_grade(data, args.student_id, args.course, validated_grade)
            print("Grade added successfully!")
        
        elif args.command == "list":
            items = service.list_students(data, args.sort) if args.type == "students" else data[args.type]
            for item in items:
                print(item)
        
        elif args.command == "avg":
            avg = service.compute_average(data, args.student_id, args.course)
            print(f"Average for student {args.student_id} in {args.course}: {avg:.2f}")

        elif args.command == "gpa":
            gpa = service.compute_gpa(data, args.student_id)
            print(f"GPA for student {args.student_id}: {gpa:.2f}")

        storage.save_data(data)
    
    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        logging.error(f"CLI Error: {e}")
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()