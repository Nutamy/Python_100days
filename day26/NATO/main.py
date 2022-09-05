import pandas as pd
student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

student_data_frame = pd.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

nato = pd.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for index, row in nato.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = list(input("Enter a word: "))
word_list = [nato_dict[letter.upper()] for letter in word]
print(word_list)



#
# nato = pd.read_csv("nato_phonetic_alphabet.csv")
# phonetic_dict = {row.letter: row.code for index, row in nato.iterrows()}
# print(phonetic_dict)










# letters = []
# codes = []
# for row in data[1:]:
#     letters.append(row.split(",")[0])
#     codes.append(row.split(",")[1][:-1])
# new_d = {
#     "letter": letters,
#     "code": codes
# }
#
# df = pd.DataFrame(new_d)
# print(df)