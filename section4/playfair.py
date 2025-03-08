import string

# 1) Read keyword and normalize it
keyword = input("Enter the keyword: ").replace(" ", "").upper()
# Convert 'J' to 'I' (classic approach that merges I/J in the same slot)
keyword = keyword.replace("J", "I")

# 2) Build the 5x5 matrix
matrix_list = []
for ch in keyword:
    if ch not in matrix_list and ch in string.ascii_uppercase:
        matrix_list.append(ch)

# Fill remaining letters of alphabet (skipping 'J' or merging it into 'I')
for ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    if ch == 'J':
        continue  # skip 'J' entirely
    if ch not in matrix_list:
        matrix_list.append(ch)

# 3) Display the 5x5 matrix
print("\nPlayfair Matrix (5x5):")
for i in range(5):
    row = matrix_list[i*5:(i+1)*5]
    print(" ".join(row))

# 4) Ask user whether to Encrypt or Decrypt
mode = input("\nDo you want to (E)ncrypt or (D)ecrypt? ").upper()
while mode not in ["E", "D"]:
    mode = input("Invalid choice. Enter 'E' for Encrypt or 'D' for Decrypt: ").upper()

# 5) Read the message, normalize it
message = input("Enter the message: ")
message = message.upper().replace(" ", "")
# Merge 'J' into 'I' for processing
message = message.replace("J", "I")

# 6) Create a lookup (letter -> (row, col)) to speed up position-finding
positions = {}
for index, letter in enumerate(matrix_list):
    row = index // 5
    col = index % 5
    positions[letter] = (row, col)

# 7) Split into digraphs (pairs), inserting 'X' between repeated letters
processed = []
i = 0
while i < len(message):
    ch1 = message[i]
    # Skip non-alphabetic (if any)
    if ch1 not in string.ascii_uppercase:
        i += 1
        continue
    
    # If this is the last char, pad with 'X'
    if i == len(message) - 1:
        processed.append(ch1)
        processed.append('X')
        i += 1
    else:
        ch2 = message[i + 1]
        if ch2 not in string.ascii_uppercase:
            # If next char isn't alphabetic, just pair ch1 with 'X'
            processed.append(ch1)
            processed.append('X')
            i += 1
        else:
            # If both letters are the same, insert 'X' after first letter
            if ch1 == ch2:
                processed.append(ch1)
                processed.append('X')
                i += 1
            else:
                processed.append(ch1)
                processed.append(ch2)
                i += 2

# 8) Encrypt/Decrypt each pair using Playfair rules
result = []
for i in range(0, len(processed), 2):
    ch1 = processed[i]
    ch2 = processed[i+1]
    r1, c1 = positions[ch1]
    r2, c2 = positions[ch2]
    
    if r1 == r2:
        # Same row
        if mode == 'E':
            # Shift right (wrap around)
            c1 = (c1 + 1) % 5
            c2 = (c2 + 1) % 5
        else:
            # Shift left (wrap around)
            c1 = (c1 - 1) % 5
            c2 = (c2 - 1) % 5
    elif c1 == c2:
        # Same column
        if mode == 'E':
            # Shift down
            r1 = (r1 + 1) % 5
            r2 = (r2 + 1) % 5
        else:
            # Shift up
            r1 = (r1 - 1) % 5
            r2 = (r2 - 1) % 5
    else:
        # Rectangle swap: same row, other letter's column
        temp = c1
        c1 = c2
        c2 = temp
    
    # Find the new letters from updated positions
    new_ch1 = matrix_list[r1 * 5 + c1]
    new_ch2 = matrix_list[r2 * 5 + c2]
    result.append(new_ch1)
    result.append(new_ch2)

# 9) Join and output the final text
output = "".join(result)
print("\nResult:", output)
