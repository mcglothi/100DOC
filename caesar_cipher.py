from caesar_art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
continue_program = True

print(logo) # Print the logo 

while continue_program:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  def caesar(text, shift, direction):
    result = ""
    for letter in text:
      if letter in alphabet:
        index = alphabet.index(letter)
        if direction == "encode":
          new_index = (index + shift) % 26
        elif direction == "decode":
          new_index = (index - shift) % 26
        result += alphabet[new_index]
      else:
        result += letter
    print(f"The output is {result}")

  caesar(text=text, shift=shift, direction=direction)
  continue_program = input("Type 'y' to continue, type 'n' to quit:\n").lower
  if continue_program == "n":
    continue_program = False





