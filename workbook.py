from openpyxl import Workbook

workbook = Workbook()

sheet = workbook.active

sheet.title= "students"

sheet.append(["Roll No","Name","Class","Marks"])

students=[
    [1, "Ahmed", 7, 75],
    [2, "Ali", 9, 85],
    [3, "Taha", 8, 78],
    [4, "Irfan", 8, 80],
    [5, "Hassan", 9, 88],
    [6, "Usman", 7, 72],
    [7, "Bilal", 8, 82],
    [8, "Hamza", 9, 90],
    [9, "Zain", 6, 68],
    [10, "Danish", 8, 84]
]

for student in students:
    sheet.append(student)

workbook.save("students.xlsx")

print("Data saved in excel")