from collections import namedtuple
import csv
f = open("./data/collections/users.csv", "r")
next(f)
reader = csv.reader(f)
student_list = []
for row in reader:
    student_list.append(row)
    print(row)
coloumns = ["user_id", "integration_id", "login_id", "password", "first_name", "last_name", "full_name", "sortable_name", "short_name",
"email", "status"]
Student = namedtuple('Student', " ".join(coloumns))
student_namedtupe_list = []
for row in student_list:
    student = Student(*row)
student_namedtupe_list.append(student)
print(student_namedtupe_list)
print(student_namedtupe_list[0].full_name)
