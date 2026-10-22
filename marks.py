mark = []
def Add_student_details():
    name = str(input("enter your name"))
    total_marks=int(input("enter your marks"))
    marks ={"name":name,"total_marks":total_marks}
    mark.append(marks)
    print("student details added successfully")
def view_student_details():
    if len(mark)==0:
        print("no records found")
    else:
        for j in mark:
            print(j)
def average_marks():
        total =0
        for i in mark:
            total = total+i["total_marks"]
        average= total/len(mark)
        print("average marks",average)
while True:
    print("1.Add student")
    print("2.View student")
    print("3.Average marks")
    print("4.Save and exit")
    choice = input("enter your choice:")
    if choice == "1":
        Add_student_details()
    elif choice== "2":
        view_student_details()
    elif choice== "3":
        average_marks()
    elif choice== "4":
        break
    else:
        print("invalid choice")
            