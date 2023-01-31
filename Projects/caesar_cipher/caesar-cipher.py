from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#Chunky ass way of doing this:

# def encrypt(plain_text,shift_amount):        #word = "boring" shift = 8
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)        #position of b in the alphabet index is 1
#         new_position = position + shift_amount         #new position is 1 + shift = 9
#         new_letter = alphabet[new_position]            #new letter is shifted all by 8, word becoming "jwzqvo"
#         cipher_text += new_letter                #Append that new shifted letter to the end of the cipher_text string
#     print(f"The encoded text is {cipher_text}") 

# def decrypt(encoded_text,shift_amount):
#     decoded_text=""
#     for letter in encoded_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         new_letter = alphabet[new_position]
#         decoded_text += new_letter
#     print(f"The encoded text is {decoded_text}")

# if direction == "encode":
#     encrypt(plain_text=text,shift_amount=shift) #Set plain_text = text and shift_amount = shift
# elif direction == "decode":
#     decrypt(encoded_text=text,shift_amount=shift)

#Concise way

def caesar(start_text,shift_amount,cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
            shift_amount *= -1
    for letter in start_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        end_text += alphabet[new_position]
    print(f"The {cipher_direction}d text is {end_text}")

def loop():
    condition = input("Do you want to go again? Type 'yes' or 'no': ")
    if condition == "yes":
        caesar(text,shift,direction)

caesar(start_text=text,shift_amount=shift,cipher_direction=direction)
loop()