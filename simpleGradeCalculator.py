math_score = int(input("Masukan nilai Matematikamu : "))
english_score = int(input("Masukan nilai English : "))
science_score = int(input("Masukan nilai Science : "))
total_subject = 3

total_score= math_score + english_score + science_score
average_score = total_score / total_subject

if average_score >= 90:
    grade = 'A'
elif average_score >= 80:
    grade = 'B'
elif average_score >= 70:
    grade = 'C'
elif average_score >= 60:
    grade = 'D'
else:
    grade = 'F'

print(f"Math Score: {math_score}")
print(f"English Score: {english_score}")
print(f"science score : {science_score}")
print(f"Average Score: {average_score}")
print(f"Your Grade: {grade}")