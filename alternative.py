# String to be manipulated and new string holder
string = "Learning to code in Python"
new_string = ""

# Iterate over the initial string and capitalise every second letter
for i in range(len(string)):
    if i % 2 == 0:
        new_string += string[i].upper()
    else:
        new_string += string[i]

print(new_string)

# Split the original string so we can target individual words and make every alternate work capitalised
words = string.split()
for i in range(len(words)):
    if i % 2 == 0:
        words[i] = words[i].upper()

# Join the updated words back into a string
split_string = " ".join(words)

print(split_string)