def score(marks):
    if marks > 100:
        print("very good")
    elif marks <= 100 and marks >= 90:
        print("you have scored an A+",exam_result)
    elif marks >= 80:
        print("you have scored an A",exam_result)
    elif marks <= 70:
        print("you have scored an B+",exam_result)
    else:
        print("you have failed",exam_result)
exam_result = int(input("enter marks:"))
score(exam_result)