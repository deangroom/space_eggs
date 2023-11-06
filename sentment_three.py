# Collect student input and save it to a text file
student_data = []

while True:
    student_input = input("Enter student data (or type 'exit' to finish): ")
    if student_input.lower() == 'exit':
        break
    student_data.append(student_input)

with open('student_data.txt', 'w') as file:
    for data in student_data:
        file.write(data + '\n')
