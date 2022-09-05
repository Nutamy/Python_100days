#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
guests = []
with open("Input/Names/invited_names.txt", "r") as list_of_names:
    names = list_of_names.readlines()
    for guest in names:
        guests.append(guest)

letter_template = ""
with open("Input/Letters/starting_letter.txt", "r") as pattern_letter:
    letter_template = pattern_letter.read()

for guest in guests:
    with open(f"Output/ReadyToSend/letter_for_{guest[:-1]}.txt", "w") as letter_to_send:
        letter_to_send.write(letter_template.replace("[name]", guest[:-1]))


#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp