# def caesar_cipher_encrypt(text, shift):

text = alphabet(alpha)
shift = int(input("Please enter the number of places to shift:"))
plain text = input("Please enter a sentence:")
plain_text = plain text.ord('A') if char.isupper() else ord('a')

encrypted_text = ""

for char in plain_text:
     if char.isalpha():  # Check if the character is a letter
          index = alpha.find(char)
          index = (index + shift) % 26
	  char = alpha(index)
    
        else:
            # Keep special characters unchanged
            encrypted_text += char
    return encrypted_text

# Ask the user for a plain text sentence
plain_text = input("Enter the text to be encrypted: ")
shift = 5  # Right shift of 5

# Encrypt the text
encrypted_text = caesar_cipher_encrypt(plain_text, shift)
print("Encrypted text:", encrypted_text)
