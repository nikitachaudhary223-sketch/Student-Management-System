students={}
while True:
  print("========================================")
  print("    STUDENT MANAGEMENT SYSTEM")
  print("========================================")

  print("1. Add Student")
  print("2. View All Students")
  print("3. Search Student")
  print("4. Add Subject")
  print("5. Add Marks")
  print("6. Calculate Average")
  print("7. Check Pass/Fail")
  print("8. Find Highest Marks")
  print("9. Find Lowest Marks")
  print("10. Count Words in Student Name")
  print("11. Show Unique Subjects")
  print("12. Show Student Summary")
  print("13. Exit")

  choice=int(input("Enter what you want to do:"))

  if choice==1:
    print("Student added successfully")

  elif choice==2:
    print("Viewed student successfully")

  elif choice==3:
    print("Search student")

  elif choice==4:
   print("Subject added successfully")

  elif choice==5:
   print("Marks added successfully")

  elif choice==6:
   print("Average marks")

  elif choice==7:
   print("Pass or fail")

  elif choice==8:
   print("Highest mark")

  elif choice==9:
   print("Lowest marks")

  elif choice==10:
   print("Count words ")

  elif choice==11:
   print("Show unique subject")

  elif choice==12:
   print("Student summary")

  elif choice==13:
   print("Exit")
   break

  else:
   print("Invalid choice")


def add_students():
  name=input("Enter your name:")
  age=int(input("Enter your age"))

  students[name]={
     "age":age,
     "subjects":[],
     "marks":[]
   }
  
  print("Student added successfully")

 
def view_students():
 for name in students:
  print("Name:",name)
  print("Age:",students[name]["age"])
  print("Subjects:", students[name]["subjects"])
  print("Marks:", students[name]["marks"])
  print("--------------------")

def search_student():
 name=input("Enter student name:")

 if name in students:
  print("Name:",name)
  print("Age:",students[name]["age"])
  print("Subjects:", students[name]["subjects"])
  print("Marks:", students[name]["marks"])

 else:
   print("Student not found")
  

def add_subjects():
 name=input("Enter student name:")

 if name in students:
  subject=input("Enter subject:")

  students[name]["subjects"].append(subject)

  print("Subject added successfully")
 else:
  print("student not found")

def add_marks():
    name = input("Enter student name: ")

    if name in students:
        mark = float(input("Enter marks: "))

        students[name]["marks"].append(mark)

        print("Marks added successfully")
    else:
        print("Student not found")

def calculate_average():
    name = input("Enter student name: ")

    if name in students:
        marks = students[name]["marks"]

        if len(marks) > 0:
            total = 0

            for mark in marks:
                total = total + mark

            average = total / len(marks)

            print("Average:", average)
        else:
            print("No marks available")
    else:
        print("Student not found")

def check_pass_or_fail():
    name = input("Enter student name: ")

    if name in students:
        marks = students[name]["marks"]

        if len(marks) > 0:
            average = sum(marks) / len(marks)

            if average >= 40:
                print("Pass")
            else:
                print("Fail")
        else:
            print("No marks available")
    else:
        print("Student not found")

def highest_marks():
    name = input("Enter student name: ")

    if name in students:
        marks = students[name]["marks"]

        if len(marks) > 0:
            highest = marks[0]

            for mark in marks:
                if mark > highest:
                    highest = mark

            print("Highest mark:", highest)
        else:
            print("No marks available")
    else:
        print("Student not found")

def lowest_marks():
    name = input("Enter student name: ")

    if name in students:
        marks = students[name]["marks"]

        if len(marks) > 0:
            lowest = marks[0]

            for mark in marks:
                if mark < lowest:
                    lowest = mark

            print("Lowest mark:", lowest)
        else:
            print("No marks available")
    else:
        print("Student not found")

def count_words():
    name = input("Enter student name: ")

    words = name.strip().split()

    print("Number of words:", len(words))

def unique_subjects():
    unique = set()

    for name in students:
        for subject in students[name]["subjects"]:
            unique.add(subject)

    print("Unique subjects:", unique)

def student_summary():
    name = input("Enter student name: ")

    if name in students:
        print("==============================")
        print("Student Summary")
        print("==============================")

        print("Name:", name)
        print("Age:", students[name]["age"])
        print("Subjects:", students[name]["subjects"])
        print("Marks:", students[name]["marks"])

        marks = students[name]["marks"]

        if len(marks) > 0:
            total = 0

            for mark in marks:
                total = total + mark

            average = total / len(marks)

            print("Average:", average)

        print("==============================")

    else:
        print("Student not found")
