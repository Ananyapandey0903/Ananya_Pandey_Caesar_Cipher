def caesar_cipher(text, shift, mode):
    result = ''
    for char in text:
        
        if char.isalpha():
           
            if char.islower():
                base = ord('a')
            else:
                base = ord('A')
            
            shifted = (ord(char) - base + shift) % 26
            
            if mode == 'encrypt':
                result += chr(base + shifted)
            elif mode == 'decrypt':
                
                result += chr(base + shifted)
        else:
            
            result += char
    return result

def main():
    while True:
        
        choice = input("Enter 'e' for encryption or 'd' for decryption: ")
        if choice.lower() not in ['e', 'd']:
            print("Invalid choice. Please enter 'e' or 'd'.")
            continue
        
        
        text = input("Enter the message: ")
        shift = int(input("Enter the shift value: "))
        
       
        if choice.lower() == 'e':
            encrypted_text = caesar_cipher(text, shift, 'encrypt')
            print("Encrypted text:", encrypted_text)
        else:
            decrypted_text = caesar_cipher(text, shift, 'decrypt')
            print("Decrypted text:", decrypted_text)
        
        # Ask if the user wants to encrypt/decrypt another message
        again = input("Do you want to encrypt/decrypt another message? (yes/no): ")
        if again.lower() != 'yes':
            break

if __name__ == "__main__":
    main()