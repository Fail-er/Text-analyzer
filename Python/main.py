"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Tomáš Kalista
email: KalistaTomas@live.com
"""

TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

users_and_passwords = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

validate = False

username = input("Ussername: ")
password = input("Password: ")

if (username in users_and_passwords and password in
     users_and_passwords[username]):
    validate = True
    print(
        f'{"_"*79}\n'
        f"Welcome to the app, {username} "
        f"We have {len(TEXTS)} texts to be analyzed.\n"
    )       

else:
    print("Unregistered user, terminating the program..")


titlecase_number = 0          # Počet slov začínajících velkým písmenem 
uppercase_number = 0          # Počet slov obsahujících jen velká písmena
lowercase_number = 0          # Počet slov začínajících malým písmenem  
digit_string_number = 0       # Počet číselných řetězců
total_digit_count = 0         # Celkový součet číselných řetězců
total_word_len_count = dict() # Slovník s počtem výskytů délky slov


if validate:
    print(f'{"_"*79}')
    text_number = input(f"Enter a number btw. 1 and {len(TEXTS)} to select: ")     
    
    # Kontrola formátu zadání
    if int(text_number) > len(TEXTS)\
        or text_number < "1":
        print("Invalid number, terminating the program..")

    elif not text_number.isdigit():
        print("Input must be a number, terminating the program..")
    
    elif (text_number.isdigit() and int(text_number)
        in range(1, len(TEXTS) + 1)):
        
        # Výpočet počtu slov začínajících velkým písmenem        
        for titlecase in TEXTS[int(text_number) - 1].split(): 
            if titlecase.istitle():
                titlecase_number += 1
        
        # Výpočet počtu slov obsahujících jen velká písmena
        for uppercase in TEXTS[int(text_number) - 1].split():
            if uppercase.isupper():
                uppercase_number += 1
        
        # Výpočet počtu slov začínajících malým písmenem
        for lowercase in TEXTS[int(text_number) - 1].split():
            if lowercase.islower():
                lowercase_number += 1
        
        # Výpočet počtu číselných řetězců
        for digit_string in TEXTS[int(text_number) - 1].split():
            if digit_string.isdigit():
                digit_string_number += 1
        
        # Výpočet celkového součtu číselných řetězců
        for digit_string in TEXTS[int(text_number) - 1].split():
            if digit_string.isdigit():
                total_digit_count += int(digit_string)
        
        # Vytvoření slovníku s počtem výskytů délky slov
        for word in TEXTS[int(text_number) - 1].split():
            total_word_len_count.update({
                len(word): total_word_len_count.get(len(word), 0) + 1
            }) 
        
        print(
            f"There are {len(TEXTS[int(text_number) - 1].split())} words "
            f"in the selected text.\n"
            f"There are {titlecase_number} titlecase words.\n"
            f"There are {uppercase_number} uppercase words.\n"
            f"There are {lowercase_number} lowercase words.\n"
            f"There are {digit_string_number} numeric strings.\n"
            f"The sum of all the numbers {total_digit_count}.\n"
            f"{'_' * 79}\n"
            f"LEN|{' ' * 2}OCCURENCES{' ' * 2}|NR.\n"
            f"{'_' * 79}\n"
        )
        
        for length, occurrences in total_word_len_count.items():
            print(f"{length}| {'*' * occurrences} {occurrences}")
