# gradebook_project
This document contains all instructions for setting up, running, and testing the Gradebook application.

Setup & Virtual Environment
Follow these steps to prepare your environment:

Step 1: Create the Environment
Open your terminal in the gradebook_project folder and run:

Windows: python -m venv venv

Mac/Linux: python3 -m venv venv

Step 2: Activate the Environment
Windows (PowerShell): * Run this first if it doesn't work: Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process

Then Windows: .\venv\Scripts\activate

Mac/Linux: source venv/bin/activate

Running the Application
Phase 1: Seed the Data
Create the initial database so you have something to work with:

PowerShell/Terminal
python scripts/seed.py
Phase 2: Use the CLI (Example Commands)
List Students: python main.py list students --sort name

Add a Student: python main.py add-student --name "John Wick"

Enroll in Course: python main.py enroll --student-id 1 --course CS101

Add a Grade: python main.py add-grade --student-id 1 --course CS101 --grade 98.5

Check Average: python main.py avg --student-id 1 --course CS101

Check GPA: python main.py gpa --student-id 1

Testing & Verification
Run Unit Tests
To verify the service logic and edge cases:

PowerShell/Terminal
python -m unittest tests/test_service.py
Check Logs
Open logs/app.log to see a history of all saved data and system errors.

Design Decisions & Limitations:
Design Decisions:
Layered Architecture: Separates data rules (Models), logic (Service), and storage (Storage).

Fail-Fast Validation: Grades are checked via parse_grade immediately. If they aren't 0-100, the program stops the error before it's saved.

Friendly Errors: The CLI catches ValueErrors so the user sees a helpful message instead of a code crash.

Limitations:
Concurrent Writes: Only one person should use the app at a time to prevent data overwriting.

In-Memory Storage: The entire JSON file is loaded into RAM, which is fast for small data but limited for millions of records.

Simple GPA: Calculates the mean of course averages without credit-hour weighting.