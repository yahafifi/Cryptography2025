def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift if mode == 'encrypt' else -shift
            ascii_offset = 65 if char.isupper() else 97
            result += chr((ord(char) - ascii_offset + shift_amount) % 26 + ascii_offset)
        else:
            result += char
    return result


def vigenere_cipher(text, keyword, mode='encrypt'):
    result = ""
    keyword_repeated = (keyword * (len(text) // len(keyword) + 1))[:len(text)]
    
    for i, char in enumerate(text):
        if char.isalpha():
            shift = ord(keyword_repeated[i].lower()) - 97
            shift = shift if mode == 'encrypt' else -shift
            ascii_offset = 65 if char.isupper() else 97
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char
    return result


def main():
    while True:
        print("\nChoose an option:")
        print("1. Encryption")
        print("2. Decryption")
        print("3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '3':
            print("Exiting program. Goodbye!")
            break
        elif choice not in ['1', '2']:
            print("Invalid choice, please try again.")
            continue
        
        mode = 'encrypt' if choice == '1' else 'decrypt'
        
        print("\nChoose a cipher:")
        print("1. Caesar Cipher")
        print("2. Vigenere Cipher")
        cipher_choice = input("Enter your choice: ")
        
        if cipher_choice == '1':
            text = input("Enter the plain text: ")
            shift = int(input("Enter the shift value: "))
            result = caesar_cipher(text, shift, mode)
        elif cipher_choice == '2':
            text = input("Enter the plain text: ")
            keyword = input("Enter the keyword: ")
            result = vigenere_cipher(text, keyword, mode)
        else:
            print("Invalid choice, please try again.")
            continue
        
        print(f"Result: {result}")

if __name__ == "__main__":
    main()
