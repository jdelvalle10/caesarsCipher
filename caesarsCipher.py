# This is a Python script that prompts the user for a plain text message and a key, and returns the ciphered version using the Caesar's Cipher method.

# First we prompt the user for the plain text message and the key
plainText = input("Enter the plain text message: ")
key = int(input("Enter the key: "))


# Now we define a function that will take the plain text message and the key and return the ciphered message

def caesarsCipher(plainText, key):
    cipherText = ""
    for char in plainText:
        # Let's check if the character is a letter
        if char.isalpha():
            # Let's check if the character is upper or lower case
            if char.islower():
                # chr returns the character that corresponds to the ASCII code
                # ord returns the ASCII code that corresponds to the character
                # We use the ASCII code to shift the character by the key
                # We use the modulo operator to wrap around the alphabet
                cipherText += chr((ord(char) + key - 97) % 26 + 97)
            else:
                cipherText += chr((ord(char) + key - 65) % 26 + 65)
        else:
            cipherText += char
    return cipherText

# Now we call the function and print the result
print(caesarsCipher(plainText, key))

# We can use the same function to decipher the message by using the negative key
print("To test the decipher function, enter the ciphered message and the negative key")
cipher = input("Enter the ciphered message: ")
key = int(input("Enter the key: "))

print(caesarsCipher(cipher, key))

