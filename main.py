
import pandas as pd
import numpy as np

from functions import (
    calculate_total,
    calculate_average,
    calculate_grade,
    calculate_result
)


# 1. Load student dataset
df = pd.read_csv("students.csv")

print("=" * 60)
print("       STUDENT PERFORMANCE ANALYTICS SYSTEM")
print("=" * 60)

# 2. Display the dataset
print("\nSTUDENT DATASET")
print(df.to_string(index=False))

# 3. Define subject columns
subjects = ["Python", "AI", "Mathematics"]

# 4. Calculate total and average marks
df["Total_Marks"] = df[subjects].sum(axis=1)

# Use NumPy for numerical calculations
df["Average_Marks"] = np.round(
    np.mean(df[subjects].to_numpy(), axis=1), 2
)

# 5. Calculate grade and pass/fail using functions
df["Grade"] = df["Average_Marks"].apply(calculate_grade)

df["Result"] = df[subjects].apply(
    lambda row: calculate_result(row.tolist()), axis=1
)

# 6. Display complete student results
print("\n\nSTUDENT RESULTS")
print(
    df[
        [
            "Student_ID", "Name", "Department",
            "Total_Marks", "Average_Marks",
            "Grade", "Result", "Attendance"
        ]
    ].to_string(index=False)
)

# 7. Overall class performance
print("\n\nOVERALL CLASS ANALYSIS")

print("Total Students:", len(df))
print("Class Average:", round(df["Average_Marks"].mean(), 2))
print("Highest Average:", df["Average_Marks"].max())
print("Lowest Average:", df["Average_Marks"].min())

# 8. Pass/fail statistics
passed = (df["Result"] == "Pass").sum()
failed = (df["Result"] == "Fail").sum()

print("\nPASS/FAIL STATISTICS")
print("Students Passed:", passed)
print("Students Failed:", failed)

# 9. Subject-wise performance
print("\nSUBJECT-WISE AVERAGES")

subject_averages = df[subjects].mean()

for subject, average in subject_averages.items():
    print(f"{subject}: {average:.2f}")

best_subject = subject_averages.idxmax()
worst_subject = subject_averages.idxmin()

print("Best Performing Subject:", best_subject)
print("Lowest Performing Subject:", worst_subject)

# 10. Top 5 performers
print("\nTOP 5 PERFORMING STUDENTS")

top_students = df.nlargest(5, "Average_Marks")

print(
    top_students[
        ["Student_ID", "Name", "Average_Marks", "Grade"]
    ].to_string(index=False)
)

# 11. Attendance analysis
print("\nATTENDANCE ANALYSIS")

print("Average Attendance:", round(df["Attendance"].mean(), 2))

low_attendance = df[df["Attendance"] < 75]

print("\nStudents with attendance below 75%:")

if low_attendance.empty:
    print("No students found.")
else:
    print(
        low_attendance[
            ["Student_ID", "Name", "Attendance"]
        ].to_string(index=False)
    )

# 12. Department-wise performance
print("\nDEPARTMENT-WISE AVERAGES")

department_averages = df.groupby("Department")[
    "Average_Marks"
].mean()

print(department_averages.round(2).to_string())

# 13. Save final results to a new CSV file
df.to_csv("student_results.csv", index=False)

print("\nFinal results saved to student_results.csv")
print("\nProject executed successfully!")
