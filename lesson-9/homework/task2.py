import csv

# Create the grades.csv file with the given data
with open("grades.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Subject", "Grade"])
    writer.writerow(["Alice", "Math", 85])
    writer.writerow(["Bob", "Science", 78])
    writer.writerow(["Carol", "Math", 92])
    writer.writerow(["Dave", "History", 74])

# Read data from grades.csv and store it in a list of dictionaries
grades = []
with open("grades.csv", mode="r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        grades.append(row)

# Calculate the average grade for each subject
subject_grades = {}
for grade in grades:
    subject = grade["Subject"]
    grade_value = int(grade["Grade"])
    if subject not in subject_grades:
        subject_grades[subject] = []
    subject_grades[subject].append(grade_value)

average_grades = {
    subject: sum(grades) / len(grades) for subject, grades in subject_grades.items()
}

# Write the average grades to average_grades.csv
with open("average_grades.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Subject", "Average Grade"])
    for subject, average in average_grades.items():
        writer.writerow([subject, average])
