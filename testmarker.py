fname_answers = 'answers1.txt'
fhand_answers = open(fname_answers)

fname_student = 'ainhoa1.txt'
fhand_student = open(fname_student)

answers = {}
student = {}

for line in fhand_answers:
    line_list = line.split()
    answers.update({int(line_list[0][:-1]): line_list[1]})

qlist = []
qans = []

for line in fhand_student:
    if line[0].isdigit():
        first_line = line.split('.')
        question_number = first_line.pop(0)
        qlist.append(question_number)
    else:
        second_line = ''.join(line.split())
        if not second_line == '':
            qans.append(second_line.lower())

for i, j in zip(qlist, qans):
    student.update({int(i): j})
   
for key in answers:
    next_key = key + 1
    if next_key not in student:
        student.setdefault(next_key, 'QUESTION NOT ANSWERED')

student.popitem()

answers_tuples = list(answers.items())
student_tuples = list(student.items())

sorted_student_tuples = sorted(student_tuples, key=lambda x: x[0])

marks = 0
for i, j in zip(answers_tuples, sorted_student_tuples):
    if i == j:
        marks += 1
        print(f"Question {i[0]} correct! Correct answer: {i[1]}. Student's answer: {j[1]}.")
    else:
        print(f"Error in question number {i[0]}. Correct answer: {i[1]}. Student's answer: {j[1]}.")

print('\n')
print(f'Total: {marks / 2}/10')    
print('\n')   