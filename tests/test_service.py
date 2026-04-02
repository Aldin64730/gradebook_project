import unittest
from gradebook.service import add_course, add_grade, add_student, compute_average

class TestGradebookService(unittest.TestCase):
    def setUp(self):
        """
        Set up a fresh data dictionary before every test.
        """
        self.sample_data = {
            "students": [],
            "courses": [],
            "enrollments": []
        }

    def test_add_student_success(self):
        """Test that a student is added correctly and returns a valid ID."""
        new_id = add_student(self.sample_data, "John Doe")
        self.assertEqual(new_id, 1)
        self.assertEqual(len(self.sample_data["students"]), 1)
        self.assertEqual(self.sample_data["students"][0]["name"], "John Doe")

    def test_add_grade_success(self):
        """Test adding a grade to an existing enrollment."""
        self.sample_data["enrollments"].append({
            "student_id": 1,
            "course_code": "CS101",
            "grades": []
        })

        add_grade(self.sample_data, 1, "CS101", 95.0)
        self.assertIn(95.0, self.sample_data["enrollments"][0]["grades"])

    def test_compute_average_success(self):
        """Test that the average is calculated correctly."""
        self.sample_data["enrollments"].append({
            "student_id": 1,
            "course_code": "CS101",
            "grades": [80.0, 90.0, 100.0]
        })
        
        avg = compute_average(self.sample_data, 1, "CS101")
        self.assertEqual(avg, 90.0)

    def test_add_grade_invalid_enrollment(self):
        """Test that adding a grade fails if the enrollment doesn't exist."""
        with self.assertRaises(ValueError):
            add_grade(self.sample_data, 1, "MATH101", 85.0)

if __name__ == "__main__":
    unittest.main()