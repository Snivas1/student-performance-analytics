# STUDENT PERFORMANCE ANALYTICS SYSTEM

## Project Documentation Report

**EWB Courses | Python with AI Internship**

- **Student Name:** Shanaboina Nivas
- **Roll Number:** 23K81A66G8
- **Department / College:** CSE (AI & ML) / St. Martin’s Engineering College
- **Submission Date:** 16-10-2026

## 1. Project Title

Student Performance Analytics System

## 2. Objective

The objective of this project is to build a Python-based system that reads student records and analyzes academic performance. It calculates total and average marks, assigns grades, identifies pass/fail results, summarizes subject-wise performance, identifies top-performing students, analyzes attendance, and saves processed results to a CSV file.

## 3. Technologies Used

- **Python** — program logic, conditions, loops, and functions.
- **NumPy** — numerical calculations on subject marks.
- **Pandas** — CSV reading, DataFrame operations, filtering, grouping, and analysis.
- **CSV** — storage of input student records and output results.
- **Visual Studio Code** — development environment.
- **GitHub** — repository hosting and project submission.

## 4. Dataset Description

The input dataset is stored in `students.csv` and contains 20 sample student records. Fields include `Student_ID`, `Name`, `Department`, Python marks, AI marks, Mathematics marks, and Attendance. The program uses the three subject-mark columns to calculate totals, averages, grades, and results.

## 5. Implementation

1. **Load the dataset:** Pandas reads `students.csv` into a DataFrame.
2. **Calculate totals and averages:** The program calculates total marks for each student and uses NumPy to calculate average marks.
3. **Assign grades:** A reusable function assigns grades according to the average-mark thresholds defined in the code.
4. **Determine pass/fail:** A student passes when every subject mark is at least 40; otherwise, the student is marked as Fail.
5. **Analyze class performance:** The program calculates the number of students, class average, highest average, and lowest average.
6. **Analyze subjects:** The program calculates the average for each subject and identifies the highest- and lowest-average subjects.
7. **Identify top performers:** Pandas selects the five students with the highest average marks.
8. **Analyze attendance and departments:** The program lists students with attendance below 75% and calculates average performance by department.
9. **Save output:** The final processed DataFrame is written to `student_results.csv`.

## 6. Key Features

- Loads student records from a CSV dataset.
- Calculates total marks and average marks.
- Assigns grades using defined thresholds.
- Identifies pass/fail status using a per-subject minimum.
- Reports overall class performance.
- Calculates subject-wise averages.
- Displays the top five performers.
- Identifies students with attendance below 75%.
- Compares average performance by department.
- Exports processed data to `student_results.csv`.

## 7. Output / Screenshots

Add your actual screenshots in this section before final submission. Recommended screenshots:

1. **Project files:** VS Code Explorer showing `main.py`, `functions.py`, `students.csv`, `student_results.csv`, `README.md`, and the documentation file.
2. **How to run the project:** VS Code terminal showing the command `python main.py`.
3. **Student dataset:** Program output showing the input student records.
4. **Student results:** Output showing total marks, average marks, grades, and pass/fail status.
5. **Overall analysis:** Output showing overall class analysis and pass/fail statistics.
6. **Top performers and attendance:** Output showing the top five performing students and attendance analysis.
7. **Generated CSV:** `student_results.csv` opened in VS Code or a spreadsheet viewer.

> Replace this note with your actual screenshots. Do not submit empty screenshot placeholders.

## 8. Final Outcome

The project demonstrates how Python, NumPy, and Pandas can be used to analyze student academic records. The program generates summaries for marks, grades, pass/fail status, subject performance, top performers, attendance, and department-wise averages, then saves the results in a separate CSV file. Verify the output against the final run before submission.

## 9. Challenges & Learning

During setup, the program initially could not run because `main.py` had not been created in the project directory. The required files were then created in the correct folder, and the program was run successfully. This helped reinforce file organization, saving Python files, running programs from the VS Code terminal, and working with CSV data.

Learning outcomes include Python functions and conditions, loops, NumPy numerical operations, Pandas DataFrames, CSV file handling, filtering, grouping, and basic data analysis.

## 10. GitHub Repository

**Repository URL:** https://github.com/Snivas1/student-performance-analytics

## Final Checklist

- [ ] Project runs successfully.
- [ ] Input dataset is included.
- [ ] NumPy and Pandas are used.
- [ ] Functions, loops, and conditions are demonstrated.
- [ ] `README.md` is included.
- [ ] Actual output screenshots are inserted.
- [ ] GitHub repository URL is added.
- [ ] Repository is checked and the Google Form is submitted.
