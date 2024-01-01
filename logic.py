# Need variable to store 3 dart score and a control variable
dart_score = 0
count = 0

# Simple explanation to the user
print("This program will total your 3 dart score, enter the score for each dart after each throw.")

# Promp the user for the score of each dart
while count < 3:
    dart = int(input("Please enter your dart score: "))
    dart_score = dart_score + dart
    count += 1

# Here we create our if statement with logical error
if dart_score < 40:
    print("Keep practicing!")
elif dart_score <= 100:
    print("Good effort, that's a good score")
elif dart_score > 100:
    print("Wow, you are good at this!")
elif dart_score == 180:
    print("180!!!!!!")
else:
    print("Super score, you're almost a pro!")