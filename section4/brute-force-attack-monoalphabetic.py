import itertools
import string

# Prompt for ciphertext input
ciphertext = input("Enter the encrypted message: ")

# Define the lowercase English alphabet
alphabet = string.ascii_lowercase

# Initialize a counter for each permutation
permutation_count = 0

# Generate every possible permutation of the alphabet
for perm in itertools.permutations(alphabet):
    permutation_count += 1
    
    # Create a mapping from each ciphertext letter -> plaintext letter
    decrypt_map = {cipher_letter: plain_letter for cipher_letter, plain_letter in zip(alphabet, perm)}

    # Decrypt the ciphertext using the current mapping
    decrypted_text_chars = []
    for char in ciphertext:
        lower_char = char.lower()
        if lower_char in decrypt_map:
            decrypted_text_chars.append(decrypt_map[lower_char])
        else:
            # Non-alphabetic characters remain unchanged
            decrypted_text_chars.append(char)
    
    # Join decrypted characters and print the result
    decrypted_text = "".join(decrypted_text_chars)
    # print("".join(perm), end='\t')
    print(f"Permutation #{permutation_count}: {decrypted_text}")
