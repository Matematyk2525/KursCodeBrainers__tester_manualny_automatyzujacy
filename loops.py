students = ["Adam", "Jan", "Tomek", "Anna", "Paulina"]
for student in students:
    print(f"Na kursie jest {student}")
    if student == "Anna":
        break
word = "Python"
for letter in word:
    print(f"Litera w slowie to: {letter}")
students_dictionary = {"student1": "Adam", "student2": "Tomek", "student3": "Anna"}
for student in students_dictionary.values():
    print(f"W slowniku jest {student}")
for key, value in students_dictionary.items():
    print(f"W slowniku jest {key}, {value}")

for i in range(4):  # range(4), 0, 1, 2, 3
    print(i)
    if i == 2:
        break
