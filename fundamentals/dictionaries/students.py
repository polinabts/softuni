courses_dictionary = {}
students_dictionary = {}
data = input()

while True:
    if ":" not in data:
        break
    data = data.split(":")

    course = data[2]
    name = data[0]
    id_number = data[1]

    if course not in courses_dictionary:
        courses_dictionary[course] = {}
    students_dictionary = courses_dictionary[course]
    students_dictionary[name] = id_number
    courses_dictionary[course] = students_dictionary
    students_dictionary = {}

    data = input()

if "_" in data:
    data = data.replace("_", " ")

for student_name, number in courses_dictionary[data].items():
    print(f"{student_name} - {number}")