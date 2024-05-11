#!/usr/bin/env python3

# For more languages see other script: season_year_multilang.py
# You can copy "seasons" and "months" from there. We got presets
# for Arabic, Czech, German, English, Russian and many more

# Note: This variation of the script combines all lists
# with casings and special chars, in an "AND" fashion. 
# There's another version, that uses either seasons OR months
# cause the output of this script is a lot

import itertools

# Define data for multiple languages
seasons = {
    'English': ['spring', 'summer', 'fall', 'autumn', 'winter'],
    'German': ['Frühling', 'Sommer', 'Herbst', 'Winter'],
    # More languages can be added here
}

months = {
    'English': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'German': ['Januar', 'Februar', 'März', 'April', 'Mai', 'Juni', 'Juli', 'August', 'September', 'Oktober', 'November', 'Dezember'],
    # More languages can be added here
}

numbers = [str(n).zfill(4) for n in range(10000)]
special_chars = ['', '!', '@', '#', '$']  # Including empty string for no special character

# Function to create case variations
def create_case_variations(season, month, number):
    variations = []
    for s in [season.lower(), season.capitalize()]:
        for m in [month.lower(), month.capitalize()]:
            for num in [number.lower(), number.upper()]:  # Assuming numbers should be included in case variations
                variations.append(s + m + num)
    return variations

# Generate combinations for each language
for lang in seasons:
    with open(f'month_seasons_year_{lang}.txt', 'w') as file:
        for season, month, number in itertools.product(seasons[lang], months[lang], numbers):
            for sc_start, sc_mid, sc_end in itertools.product(special_chars, repeat=3):
                # Apply case variations and special characters
                for case_variation in create_case_variations(f'{sc_start}{season}', f'{sc_mid}{month}', f'{number}{sc_end}'):
                    file.write(case_variation + '\n')

print("Wordlists generated.")
