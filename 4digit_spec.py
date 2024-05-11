#!/usr/bin/env python3

# Wordlist Generator: 4 digit number with special char

import itertools

numbers = [str(n).zfill(4) for n in range(10000)]
special_chars = ['!', '@', '#', '$', '+', '-', '_', '.', ':', '§', '?', '%', '(', ')']  

with open(f'4digit_specialchar.txt', 'w') as file:
    for number in numbers:
        # Numbers only
        file.write(number + '\n')

        # Numbers + Special char in the end
        for sc_end in special_chars:
            file.write(number + sc_end + '\n')

        # Numbers + Special char in start
        for sc_start in special_chars:
            file.write(sc_start + number + '\n')

        # Numbers + Special char in start and end
        for sc_start, sc_end in itertools.product(special_chars, repeat=2):
            file.write(sc_start + number + sc_end + '\n')

print("Wordlists generated.")
