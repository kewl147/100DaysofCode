# TODO-1: Import and print the logo from art.py when the program starts.
import art

print(art.logo)

def encrypt(original_text, shift_amount):
    encrypted_text = ""
    for letter in original_text:
        position = alphabet.index(letter)
        new_position = (position + shift_amount) % 26
        encrypted_text += alphabet[new_position]
    print(f"Here is the encoded result: {encrypted_text}")

def decrypt(original_text, shift_amount):
    decrypted_text = ""
    for letter in original_text:
        position = alphabet.index(letter)
        new_position = (position - shift_amount) % 26
        decrypted_text += alphabet[new_position]   # fixed here
    print(f"Here is the decoded result: {decrypted_text}")


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    while direction not in ["encode", "decode"]:
        print("Invalid input. Please try again.")
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    while True:
        text = input("Type your message:\n").lower()
        if text.isalpha():
            break
        else:
            print("Please enter letters only (no numbers or symbols).")

    while True:
        shift_input = input("Type the shift number:\n")
        if shift_input.isdigit():
            shift = int(shift_input)
            break
        else:
            print("Please enter a valid number.\n")

    if direction == "encode":
        encrypt(text, shift)
    else:
        decrypt(text, shift)

    again = input("Would you like to play again? (yes/nno)\n").lower()
    if again != "yes":
        print("Thank you for playing.")
        break





