students = [("John", "A"), ("Jane", "3"), ("Doe", "A")]
grade_to_students = {}
for student, grade in students:
    if grade not in grade_to_students:
        grade_to_students[grade] = [student]
    else:
        grade_to_students[grade].append(student)

print(grade_to_students)
# {'A': ['John', 'Doe'], '3': ['Jane']}

#######################################
# Now, with defauLtaict:

from collections import defaultdict

students = [("John", "A"), ("Jane", "3"), ("Doe", "A")]
grade_to_students = defaultdict(list)
# ще групира студентите по оценки като използва списък като стойност за всеки ключ (оценка)
for student, grade in students:
    grade_to_students[grade].append(student)

print(grade_to_students)
# defaultdict(<class 'list'>, {'A': ['John', 'Doe'], '3': ['Jane']})
