alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def caesar(original_text, shift_amount, option):
    cipher = ""
    for letter in original_text:
        if letter not in alphabets:
            cipher += letter
        else:
            if option == "D":
                shift_amount = shift_amount * -1
            new_letters = alphabets.index(letter) + shift_amount
            new_letters %= len(alphabets)
            cipher += alphabets[new_letters]
    print(f"The result is {cipher}")

cont=True
while cont:
    encrypt_or_decrypt=input("Type 'E' for Encrypting or 'D' for Decrypting?\n ").lower()
    text=input("Type your message: \n").lower()
    shift=int(input("Type the shift number: \n"))
    caesar(original_text=text, shift_amount=shift, option=encrypt_or_decrypt)
    lp=input("Would you like to encrypt another value? Y for Yes and N for No ")
    if lp=='N':
        cont=False

