# Student Management System

students = {}

def add_student():
    name = input("Enter student name: ")

    if name in students:
        print("Student already exists!")
        return

    marks = float(input("Enter marks: "))
    students[name] = marks
    print("Student added successfully!")

def view_students():
    if not students:
        print("No students found.")
        return

    print("\nStudent List")
    print("-" * 30)

    for name, marks in students.items():
        print(f"Name: {name}")
        print(f"Marks: {marks}")
        print("-" * 30)

def search_student():
    name = input("Enter student name to search: ")

    if name in students:
        print(f"{name} scored {students[name]} marks.")
    else:
        print("Student not found.")

def update_marks():
    name = input("Enter student name: ")

    if name in students:
        marks = float(input("Enter new marks: "))
        students[name] = marks
        print("Marks updated successfully!")
    else:
        print("Student not found.")

def delete_student():
    name = input("Enter student name: ")

    if name in students:
        del students[name]
        print("Student deleted successfully!")
    else:
        print("Student not found.")

def average_marks():
    if not students:
        print("No student data available.")
        return

    total = sum(students.values())
    average = total / len(students)
    print(f"Average Marks: {average:.2f}")

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Average Marks")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_marks()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        average_marks()
    elif choice == "7":
        print("Thank you for using Student Management System.")
        break
    else:
        print("Invalid choice! Please try again.")
