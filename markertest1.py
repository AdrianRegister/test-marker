import re

fname_answers = 'answers1.txt'
fhand_answers = open(fname_answers)

fname_student = 'ainhoa1.txt'
fhand_student = open(fname_student)

answers = []

for line in fhand_answers:
    correct_answer = r"\d+\.\s*(.+)"
    correct_answer = re.match(correct_answer, line)
    if correct_answer:
        result = correct_answer.group(1)
        answers.append(result.strip())
        
student_answers = []

for line in fhand_student:
    correct_answer = r'.+'
    correct_answers = re.findall(correct_answer, line, re.DOTALL)
    for answer in correct_answers:
        if not any(answer.startswith(str(i)) for i in range(10)):
            answer = answer.lower()
            student_answers.append(answer.strip())           

for answer in student_answers:
    if answer == '':
        student_answers.remove(answer)

print('\n')

marks = 0
for i, j in zip(answers, student_answers):
    if i == j:
        marks += 1
    else:
        print(f"Error in question number {answers.index(i) + 1}. Correct answer: {i}. Student's answer: {j}.")

print('\n')
print(f'Total: {marks / 2}/10')    
print('\n')    
