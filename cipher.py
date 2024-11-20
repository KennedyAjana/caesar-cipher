alphabet = "abcdefghijklmnopqrstuvwxyz"

shift = int(input("Please enter number of places to shift:"))
plain_text= input("Please enter a sentence: ")

encrypted_text = ""

for char in plain_text:
     if char in alphabet:
          index = alphabet.find(char)
          index = (index + shift) % 26
          char = alphabet[index]
     encrypted_text += char

print(encrypted_text)
