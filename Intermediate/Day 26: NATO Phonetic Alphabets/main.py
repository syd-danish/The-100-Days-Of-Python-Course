import pandas

# TODO 1. Create a dictionary in this format:
nato_dict = pandas.read_csv("nato_phonetic_alphabet.csv")
dictionary = {nato_dict.letter.to_list()[i]: nato_dict.code.to_list()[i] for i in range(0, len(nato_dict.code.to_list()))}
print(dictionary)
while True:
    # TODO 2. Create a list of the phonetic code words from a word that the user inputs.
    Input = input("Enter a word:").upper().replace(" ", "")
    phonetic_list = [dictionary[i] for i in Input]
    print(phonetic_list)
