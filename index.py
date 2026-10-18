
import os
import sys

# 1. Student Information
Name = "Fakhar"
Age = 20
Course = "ADSE1"
Institute = "Aptech Start Gate"
City = "Karachi"
Location = "Model Colony"

# Dictionary
Student = {
    "Name": Name,
    "Age": Age,
    "Course": Course,
    "Institute": Institute,
    "City": City,
    "Location": Location
}

print("===== Student Dictionary =====")
print(Student)


# 2. Dictionary ko List mein convert karna
Student_List = list(Student.items())
print("\n===== Student List =====")
print(Student_List)


# 3. List Methods
Student_List.insert(2, ("Status", "OK"))
print("\nIndex of Status:", Student_List.index(("Status", "OK")))

Student_List.append(("Extra", "King"))
Student_List.extend([
    ("Friend1", "Done"),
    ("Friend2", "Jhone"),
    ("Friend3", "Roman")
])

Student_List.pop()
Student_List = [
    item for item in Student_List
    if item[0] != "Course"
]

print("\n===== Updated List =====")
print(Student_List)


# 4. Multiple Students
Name = "Fakhar Hussain"
Age = 20
City = "Karachi"

Name1 = "Fakhar"
Age1 = 22
City1 = "Karachi"

Students = [
    {
        "Name": Name,
        "Age": Age,
        "City": City
    },
    {
        "Name": Name1,
        "Age": Age1,
        "City": City1
    }
]

# Add Course to first student
Students[0]["Course"] = "ADSE1"

# Add another student
Students.append({
    "Name": "Ali",
    "Age": 21,
    "City": "Karachi",
    "Course": "ADSE1"
})

# Extend list
Students.extend([
    {
        "Name": "Ahmed",
        "Age": 23,
        "City": "Lahore"
    }
])

print("\n===== All Students =====")
for student in Students:
    print(student)


# 5. Even / Odd Function
def check_list():
    num = int(input("\nEnter number: "))

    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")


check_list()


# 6. File Handling
file_path = os.path.join(os.getcwd(), "student.txt")

# Write data
with open(file_path, "w") as file:
    file.write("Name: Fakhar\n")
    file.write("Age: 20\n")
    file.write("City: Karachi\n")

# Append data
with open(file_path, "a") as file:
    file.write("Course: ADSE1\n")
    file.write("Institute: Aptech Start Gate\n")

# Read data
with open(file_path, "r") as file:
    data = file.read()

print("\n===== File Data =====")
print(data)

# Convert text into list
Student_File_List = data.split("\n")
print("===== File Data List =====")
print(Student_File_List)

print("\nProgram completed successfully!")
