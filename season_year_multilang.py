#!/usr/bin/env python3

# Wordlist Generator: season, year, many languages

import itertools

# Define data for multiple languages
seasons = {
    'English': ['spring', 'summer', 'fall', 'autumn', 'winter'],
    'German': ['Frühling', 'Sommer', 'Herbst', 'Winter'],
    'French': ['printemps', 'été', 'automne', 'hiver'],
    'Russian': ['весна', 'лето', 'осень', 'зима'],
    'Turkish': ['ilkbahar', 'yaz', 'sonbahar', 'kış'],
    'Polish': ['wiosna', 'lato', 'jesień', 'zima'],
    'Spanish': ['primavera', 'verano', 'otoño', 'invierno'],
    'Italian': ['primavera', 'estate', 'autunno', 'inverno'],
    'Dutch': ['lente', 'zomer', 'herfst', 'winter'],
    'Danish': ['forår', 'sommer', 'efterår', 'vinter'],
    'Romanian': ['primăvară', 'vară', 'toamnă', 'iarnă'],
    'Czech': ['jaro', 'léto', 'podzim', 'zima'],
    'Arabic': ['ربيع', 'صيف', 'خريف', 'شتاء']
}

months = {
    'English': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'German': ['Januar', 'Februar', 'März', 'April', 'Mai', 'Juni', 'Juli', 'August', 'September', 'Oktober', 'November', 'Dezember'],
    'French': ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre'],
    'Russian': ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь'],
    'Turkish': ['Ocak', 'Şubat', 'Mart', 'Nisan', 'Mayıs', 'Haziran', 'Temmuz', 'Ağustos', 'Eylül', 'Ekim', 'Kasım', 'Aralık'],
    'Polish': ['Styczeń', 'Luty', 'Marzec', 'Kwiecień', 'Maj', 'Czerwiec', 'Lipiec', 'Sierpień', 'Wrzesień', 'Październik', 'Listopad', 'Grudzień'],
    'Spanish': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
    'Italian': ['Gennaio', 'Febbraio', 'Marzo', 'Aprile', 'Maggio', 'Giugno', 'Luglio', 'Agosto', 'Settembre', 'Ottobre', 'Novembre', 'Dicembre'],
    'Dutch': ['Januari', 'Februari', 'Maart', 'April', 'Mei', 'Juni', 'Juli', 'Augustus', 'September', 'Oktober', 'November', 'December'],
    'Danish': ['Januar', 'Februar', 'Marts', 'April', 'Maj', 'Juni', 'Juli', 'August', 'September', 'Oktober', 'November', 'December'],
    'Romanian': ['Ianuarie', 'Februarie', 'Martie', 'Aprilie', 'Mai', 'Iunie', 'Iulie', 'August', 'Septembrie', 'Octombrie', 'Noiembrie', 'Decembrie'],
    'Czech': ['Leden', 'Únor', 'Březen', 'Duben', 'Květen', 'Červen', 'Červenec', 'Srpen', 'Září', 'Říjen', 'Listopad', 'Prosinec'],
    'Arabic': ['يناير', 'فبراير', 'مارس', 'أبريل', 'مايو', 'يونيو', 'يوليو', 'أغسطس', 'سبتمبر', 'أكتوبر', 'نوفمبر', 'ديسمبر']
    # More languages can be added here
}

numbers = [str(n).zfill(4) for n in range(10000)]
special_chars = ['', '!', '@', '#', '$']  # Including empty string for no special character

# Function to create case variations
def create_case_variations(word, number):
    variations = []
    for w in [word.lower(), word.capitalize()]:
        for num in [number.lower(), number.upper()]:  # Assuming numbers should be included in case variations
            variations.append(w + num)
    return variations

# Generate combinations for each language
for lang in seasons:
    with open(f'month_seasons_year_{lang}.txt', 'w') as file:
        # Generate combinations with either month or season
        for word, number in itertools.product(seasons[lang] + months[lang], numbers):
            for sc_start, sc_mid, sc_end in itertools.product(special_chars, repeat=3):
                # Apply case variations and special characters
                for case_variation in create_case_variations(f'{sc_start}{word}{sc_mid}', f'{number}{sc_end}'):
                    file.write(case_variation + '\n')

print("Wordlists generated.")
