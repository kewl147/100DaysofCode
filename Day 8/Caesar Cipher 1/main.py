alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

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

def encrypt(original_text, shift_amount):
    encrypted_text = ""
    for letter in original_text:
        position = alphabet.index(letter)
        new_position = (position + shift_amount) % 26
        encrypted_text += alphabet[new_position]
    print(f"Here is the encoded result: {encrypted_text}")



if direction == "encode":
    encrypt(text, shift)


