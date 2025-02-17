PLACEHOLDER='[name]'
with open ("./Input/Names/invited_names.txt") as name_file:
    names=name_file.readlines()

with open('./Input/Letters/starting_letter.txt') as letter_file:
    letter=letter_file.read()
    for name in names:
        new_letter=letter.replace(PLACEHOLDER, name.strip())
        print(new_letter)
        with open(f"./Output/ReadyToSend/letter_for_{name.strip()}.txt",'w') as completed_letter:
            completed_letter.write(new_letter)
