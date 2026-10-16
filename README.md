# Student Performance Analytics System

## Project Overview
The Student Performance Analytics System is a Python-based data analysis project developed as part of the EWB Courses Python with AI internship.

The system analyzes student marks and attendance to generate useful academic performance reports, including total marks, average marks, grades, pass/fail results, subject-wise performance, and top-performing students.

## Objectives
- Analyze student academic performance using Python.
- Calculate total and average marks.
- Assign grades based on average marks.
- Identify students who pass or fail.
- Analyze subject-wise and department-wise performance.
- Identify top-performing students.
- Save the final analysis to a CSV file.

## Technologies Used
- Python
- NumPy
- Pandas
- Visual Studio Code
- CSV files
- GitHub

## Project Structure
- `main.py` — Main program for student performance analysis.
- `functions.py` — Reusable functions for totals, averages, grades, and results.
- `students.csv` — Input dataset containing student information, marks, and attendance.
- `student_results.csv` — Generated output containing calculated results.

## Features
1. Student dataset loading and display.
2. Total and average marks calculation.
3. Automatic grade assignment.
4. Pass/fail identification.
5. Overall class performance analysis.
6. Subject-wise average calculation.
7. Top five student identification.
8. Attendance analysis.
9. Department-wise performance analysis.
10. Export of processed results to a CSV file.

## Installation and Execution

### 1. Install Python
Install Python from https://www.python.org/downloads/.

### 2. Install Required Libraries
Open the terminal in the project directory and run:

```bash
python -m pip install numpy pandas
```

### 3. Run the Project
Execute the following command:

```bash
python main.py
```

### 4. View the Results
The program displays the analysis in the terminal and automatically generates `student_results.csv`.

## Grading Rules
- A+ : Average marks >= 90
- A : Average marks >= 80
- B : Average marks >= 70
- C : Average marks >= 60
- D : Average marks >= 50
- F : Average marks < 50

A student passes if they score at least 40 marks in every subject. Otherwise, the student fails.

## Learning Outcomes
Through this project, I practiced Python fundamentals, functions, loops, conditional statements, NumPy numerical operations, Pandas DataFrames, CSV file handling, and data analysis.

## Conclusion
The Student Performance Analytics System successfully demonstrates how Python, NumPy, and Pandas can be used to process student records and generate meaningful academic performance reports.

## Author
Developed as part of the EWB Courses Python with AI internship.
