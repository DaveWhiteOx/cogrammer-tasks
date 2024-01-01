# Prompt user for how many students will need to be registered
num_students = int(input("Please enter the number of students to be registered: "))

# Loop to prompt the user for the relevent student ID numbers to record to file
for i in range(num_students):
    student_id = input("Please enter the student ID to record to file: ")

    # now write to the file and include dotted line for signatures
    with open('reg_form.txt', 'a') as f:
        f.write(student_id + " ....................." + "\n")

# Open the file and read the contents to check all is created as expected
with open('reg_form.txt', 'r') as register:
    print(register.read())