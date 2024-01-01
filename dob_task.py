# Open the file to read the contents
with open('DOB.txt', 'r') as file:

    lines = file.readlines()

    names = ""
    person_dob = ""

    # Iterate each line and split the data so we can select the relevant parts for our output
    for line in lines:
        temp = line.split()
        names = ' '.join(temp[0:2])
        person_dob += ' '.join(temp[2:])

    
    print(names)
    print(person_dob)
