def encrypt_rail_fence(text, key):
    # Initialize an empty list of strings for each rail (row)
    rail = ['' for i in range(key)]
    
    # Initialize direction flag and starting row index
    dir_down = False
    row = 0

    # Iterate through each character in the input text
    for char in text:
        # Append character to the current row
        rail[row] += char

        # Change direction if the current row is the first or last rail
        if row == 0 or row == key - 1:
            dir_down = not dir_down

        # Move to the next row based on the current direction
        if dir_down:
            row += 1
        else:
            row -= 1

    # Concatenate all rows to produce the final ciphertext
    return ''.join(rail)


def decrypt_rail_fence(cipher, key):
    # Create a 2D matrix with placeholder characters for layout simulation
    rail = [['$' for j in range(len(cipher))] for i in range(key)]

    # Initialize direction control and position indicators
    dir_down = None
    row, col = 0, 0

    # Step 1: Mark the pattern of rails using placeholders ('*')
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False

        # Place marker at the calculated position
        rail[row][col] = '*'
        col += 1
        if dir_down:
            row += 1
        else:
            row -= 1

    # Step 2: Replace placeholders with actual characters from the cipher text
    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if rail[i][j] == '*' and index < len(cipher):
                rail[i][j] = cipher[index]
                index += 1

    # Step 3: Traverse the matrix in zigzag order to reconstruct the plaintext
    result = []
    row, col = 0, 0
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False

        result.append(rail[row][col])
        col += 1
        if dir_down:
            row += 1
        else:
            row -= 1

    # Combine the characters to produce the final decrypted message
    return ''.join(result)

# Example usage
message = "HELLO WORLD"
key = 3

# Encrypting the input message (spaces removed for simplicity)
encrypted = encrypt_rail_fence(message.replace(" ", ""), key)
print("Encrypted:", encrypted)

# Decrypting the ciphertext to retrieve the original message
decrypted = decrypt_rail_fence(encrypted, key)
print("Decrypted:", decrypted)
