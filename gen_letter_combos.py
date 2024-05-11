#!/usr/bin/env python3

# Wordlist Generator: ASCII Letters, Numbers, 0-2 Special Chars

import itertools
import string

# Create a list of uppercase & lowercase chars and digits
chars_digits = list(string.ascii_letters + string.digits)

# List of special characters
special_chars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=']

# Function to generate combinations
def generate_combinations():
    with open("combinations.txt", "w") as file:
        # Generate combinations for 1 to 6 letter-digit strings
        for r in range(1, 6):
            for combo in itertools.product(chars_digits, repeat=r):
                combo_str = ''.join(combo)
                file.write(combo_str + '\n') # Write the combo without special chars

                # Add 1 special char
                for special in special_chars:
                    file.write(combo_str + special + '\n')

                # Add 2 special chars
                for special_combo in itertools.product(special_chars, repeat=2):
                    file.write(combo_str + ''.join(special_combo) + '\n')

# Run the function
generate_combinations()
