students = {}
def add_student():
    sid = input("Enter Student ID: ")

    if sid in students:
        print("Student already exists.")
        return

    name = input("Enter Student Name: ")
    course = input("Enter Course: ")

    students[sid] = {
        "name": name,
        "course": course,
        "present": 0,
        "absent": 0
    }

    print("Student Added Successfully")
    print(students)

def mark_attendance():
    sid = input("Enter Student ID: ")

    if sid not in students:
        print("Student Not Found")
        return

    print("1. Present")
    print("2. Absent")

    choice = input("Enter Choice: ")

    if choice == "1":
        students[sid]["present"] += 1
        print("Attendance Marked Present")

    elif choice == "2":
        students[sid]["absent"] += 1
        print("Attendance Marked Absent")

    else:
        print("Invalid Choice")


def attendance_percentage(sid):
    present = students[sid]["present"]
    absent = students[sid]["absent"]

    total = present + absent

    if total == 0:
        return 0

    return (present / total) * 100


def scholarship():
    sid = input("Enter Student ID: ")

    if sid not in students:
        print("Student Not Found")
        return

    percent = attendance_percentage(sid)

    print("Attendance Percentage =", round(percent, 2), "%")

    if percent >= 90:
        print("Scholarship Status : Eligible")

    elif percent >= 75:
        print("Scholarship Status : Conditional")

    else:
        print("Scholarship Status : Not Eligible")


def report():
    if len(students) == 0:
        print("No Student Records")
        return

    print("\n----- Attendance Report -----")

    for sid, details in students.items():

        percent = attendance_percentage(sid)

        print("----------------------------")
        print("Student ID :", sid)
        print("Name :", details["name"])
        print("Course :", details["course"])
        print("Present :", details["present"])
        print("Absent :", details["absent"])
        print("Attendance :", round(percent, 2), "%")

        if percent >= 90:
            status = "Eligible"
        elif percent >= 75:
            status = "Conditional"
        else:
            status = "Not Eligible"

        print("Scholarship :", status)


while True:

    print("\n===== Scholarship Attendance System =====")
    print("1. Add Student")
    print("2. Mark Attendance")
    print("3. Check Scholarship")
    print("4. Attendance Report")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        mark_attendance()

    elif choice == "3":
        scholarship()

    elif choice == "4":
        report()

    elif choice == "5":
        print("Thank You")
        break

    else:
        print("Invalid Choice")
print(students)