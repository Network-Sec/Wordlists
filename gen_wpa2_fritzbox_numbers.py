#!/usr/bin/env python3

# Wordlist Generator: For Fritz!BOX default "number passwords" (Wifi)
# It's a limited / random approach, as the entire space of 16-32 digit 
# length is not feasable with current gen hardware

import random
import time

def is_valid_number(number):
    """Check if the number has no three consecutive identical digits."""
    return all(number[i] != number[i+1] or number[i] != number[i+2] for i in range(len(number)-2))

def generate_number(length):
    """Generate a number of given length where no three consecutive digits are alike."""
    while True:
        number = [str(random.randint(0, 9)) for _ in range(length)]
        if is_valid_number(number):
            return ''.join(number)

def generate_and_write_numbers(target_size_bytes):
    lengths = [8, 12, 16, 20]
    bytes_per_length = [9, 13, 17, 21]
    total_bytes_per_set = sum(bytes_per_length)
    numbers_per_length = target_size_bytes // total_bytes_per_set

    with open("wpa2_fritzbox_numbers_10GB.txt", "w") as file:
        for length in lengths:
            written_count = 0
            last_update_time = time.time()

            while written_count * (length + 1) < numbers_per_length * (length + 1):
                number = generate_number(length)
     
                file.write(number + '\n')
                written_count += 1

                if written_count % 1000:
                    current_time = time.time()
                    if current_time - last_update_time >= 10:
                        estimated_size = (written_count * (length + 1)) / (1024 ** 3)
                        print(f"Progress for length {length}: {estimated_size:.2f} GB")
                        last_update_time = current_time

generate_and_write_numbers(10 * 1073741824)

