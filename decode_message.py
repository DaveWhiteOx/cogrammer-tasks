# The below function is used to decode a message hidden in the coding_qual_input.txt
def decode(message_file):
    with open(message_file, "r") as file:
        file_data = file.readlines()

    # Get the number of lines/words
    num_lines = len(file_data)

    # Convert to a dictionary and sort
    number_word = {}
    for line in file_data:
        number, word = line.split()
        number_word[number] = word
    
    
    # Create number groups and use last value to retrieve required word from dictionary
    nums = list(range(1, num_lines+1))
    word_list = []
    step = 1
    subset = []
    while len(nums) != 0:
        if len(nums) >= step:
            subset = (nums[0:step])
            word_list.append(number_word[str(subset[-1])])
            nums = nums[step:]
            step += 1
        else:
            return False
      
    # return the decoded words as a string
    return ' '.join(word_list)
    
        
decoded_message = decode("coding_qual_input.txt")
print(decoded_message)
