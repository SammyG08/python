
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y','z',
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']

def encryption_and_decryption(word, shift, choice):
    result = ""
    for character in word :
        if choice == "encryption":
            if character in alphabet:
                positionOfALphabet = alphabet.index(character)
                newPosition = ( positionOfALphabet + shiftKey ) % 52
                result += alphabet[newPosition] 
            elif character not in alphabet:
                result += character
                
        elif choice == "decryption":
             if character in alphabet:
                positionOfALphabet = alphabet.index(character)
                newPosition = ( positionOfALphabet - shiftKey ) % 52
                result += alphabet[newPosition] 
             elif character not in alphabet:
                result += character
            
    print (f'\nThe word after encryption is: {result}.\n')

end = False

while not end :
    userChoice = input("Type \'encrypt\' to encrypt and \'decrypt\' to decrypt.\n").lower()
    shiftKey = int(input("\nWhat is the shift key?\n"))

    if userChoice == 'encrypt':
        plaintext = input("\nWhat word will you like to encrypt?\n")
        encryption_and_decryption(plaintext, shiftKey, "encryption")
    
    elif userChoice == "decrypt":
        cipherText = input("\nWhat word will you like to decrypt?\n")
        encryption_and_decryption(cipherText, shiftKey, "decryption")
    
    option = input("\nWill you like to continue? y/n\n")
    if option == 'n':
        end = True
        print ("Goodbye and have a good day!\n")
        

        