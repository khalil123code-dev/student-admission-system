while True:
    name = input("Enter your name: ").strip()
    if name and name.replace(" ", "").isalpha():
        break
    print("Invalid input! Please enter a valid name using letters only.")
        
while True:

    try:
        age = int(input("Enter your age: "))

    except ValueError:
        print("Invalid input! Please enter a valid integer.")
        continue

    if age < 10 or age > 70:
        print("Invalid age! Please enter a realistic age between 10 and 70.")
        continue

    print("Input accepted.")
    break

if age < 18:
    print("Sorry! Your age is below the minimum requirement.")
    exit()

while True:
    try:
        grade_1 = float(input("Enter your grade in Mathematics: "))

    except ValueError:
        print("Invalid input! Please enter a valid number.")
        continue

    if grade_1 > 100 or grade_1 < 0:
        print("Invalid grade! Grade must be between 0 and 100.")
        continue

    break

while True:
    try:
        grade_2 = float(input("Enter your grade in Programming: "))

    except ValueError:
        print("Invalid input! Please enter a valid number.")
        continue

    if grade_2 > 100 or grade_2 < 0:
        print("Invalid grade! Grade must be between 0 and 100.")
        continue

    break

while True:
    try:
        grade_3 = float(input("Enter your grade in English: "))

    except ValueError:
        print("Invalid input! Please enter a valid number.")
        continue

    if grade_3 > 100 or grade_3 < 0:
        print("Invalid grade! Grade must be between 0 and 100.")
        continue

    break


max_grade = 100
num_subjects = 3
max_total = max_grade * num_subjects

total = grade_1 + grade_2 + grade_3
average = total / num_subjects
result_1 = round(average, 2)
percentage = (total / max_total) * 100
result_2 = round(percentage, 2)

min_passing_score = 50
passing_all_subjects = (grade_1 >= min_passing_score and grade_2 >= min_passing_score and grade_3 >= min_passing_score)

if average >= min_passing_score and passing_all_subjects:
    admission_status = "Accepted"
    print("Congratulations! You have been accepted.")

elif average < min_passing_score and not passing_all_subjects:
    admission_status = "Rejected"
    print("Sorry! Both your average and at least one subject are below the minimum requirement.")

elif average < min_passing_score:
    admission_status = "Rejected"
    print("Sorry! Your average is below the minimum requirement.")

else:
    admission_status = "Rejected"
    print("Sorry! At least one subject grade is below the minimum requirement.")

print("========== STUDENT REPORT ==========")

print(f"Student name: {name}")
print(f"Age: {age}")

print(f"Mathematics: {grade_1}")
print(f"Programming: {grade_2}")
print(f"English: {grade_3}")

print(f"Total Marks: {total}")
print(f"Average: {result_1}")
print(f"Percentage: {result_2}%")

print(f"Admission Status: {admission_status}")

print("====================================")
