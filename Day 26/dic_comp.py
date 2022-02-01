import random

students = ["Alex", "Beth", "Kok", "Fufu", "Zeal"]

student_scores = {student:random.randint(1,100) for student in students}
student_passed = {student:score for (student, score) in student_scores.items() if score >= 60}

print(student_passed)