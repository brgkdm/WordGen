import itertools
import random
import string
import os
import time
import sys
import logging

logging.basicConfig(filename="wordgen.log", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

def clear_screen_with_message(message):
    print("\033c", end="")  # Clear screen
    print("\033[32m")
    print(message)
    print("\033[0m")

def print_header():
    clear_screen_with_message(r"""

░██╗░░░░░░░██╗░█████╗░██████╗░██████╗░░██████╗░███████╗███╗░░██╗
░██║░░██╗░░██║██╔══██╗██╔══██╗██╔══██╗██╔════╝░██╔════╝████╗░██║
░╚██╗████╗██╔╝██║░░██║██████╔╝██║░░██║██║░░██╗░█████╗░░██╔██╗██║
░░████╔═████║░██║░░██║██╔══██╗██║░░██║██║░░╚██╗██╔══╝░░██║╚████║
░░╚██╔╝░╚██╔╝░╚█████╔╝██║░░██║██████╔╝╚██████╔╝███████╗██║░╚███║
░░░╚═╝░░░╚═╝░░░╚════╝░╚═╝░░╚═╝╚═════╝░░╚═════╝░╚══════╝╚═╝░░╚══╝
          """)
    print("\033[0m")
    print(r"""
https://github.com/brgkdm
          """)
    print("*If you create the same file twice, it will overwrite the file.")
    print("\nPress Enter.\n")
    input()

def choose_output_file():
    default_name = f"wordlist_{int(time.time())}.txt"
    clear_screen_with_message(f"\033[33m❯ Default file name: {default_name}\033[0m\n\nEnter file name (or press Enter for default): ")
    filename = input()
    if not filename:
        filename = default_name
    if not filename.endswith(".txt"):
        filename += ".txt"
    clear_screen_with_message(f"\033[32m\n***The wordlist will be saved as: {filename} in the current directory.\n\033[0m")
    time.sleep(4)
    return filename

def choose_combination_type():
    while True:
        clear_screen_with_message("\033[33m❯ Select the type of password combination to generate.\033[0m\n\n1. Words + Numbers (e.g., word123, 123word)\n2. Capitalized + Year (e.g., Word2024)\n3. Words + Special Characters (e.g., word!, word@123)\n4. Mixed Case Randomized (e.g., wOrD123)\n5. All Options Combined (recommended)")
        choice = input("\n❯ Enter your choice (1-5)?: ")

        if choice == '1':
            clear_screen_with_message("\033[32m***Words + Numbers selected\033[0m")
            time.sleep(2)
            return choice
        elif choice == '2':
            clear_screen_with_message("\033[32m***Capitalized + Year selected\033[0m")
            time.sleep(2)
            return choice
        elif choice == '3':
            clear_screen_with_message("\033[32m***Words + Special Characters selected\033[0m") 
            time.sleep(2)
            return choice
        elif choice == '4':
            clear_screen_with_message("\033[32m***Mixed Case Randomized selected\033[0m")
            time.sleep(2)
            return choice
        elif choice == '5':
            clear_screen_with_message("\033[32m***All Options Combined selected\033[0m")
            time.sleep(2)
            return choice
        else:
            clear_screen_with_message("\033[31m***Invalid choice. Please select a number between 1 and 5.\033[0m")
            time.sleep(3)

def ask_wordlist_length():
    clear_screen_with_message("\033[33m\n❯ How many words (max 1.000.000) do you want to generate?\033[0m")
    while True:
        try:
            count = int(input("❯ Number of words: "))
            if 1 <= count <= 1000000:
                return count
            else:
                clear_screen_with_message("\033[31m***Please enter a number between 1 and 1.000.000.\033[0m")
                time.sleep(3)
        except ValueError:
            clear_screen_with_message("\033[31m***Please enter a number between 1 and 1.000.000\033[0m")
            time.sleep(3)

def generate_years_combination(word, start=1900, end=2025):
    return [f"{word.capitalize()}{year}" for year in range(start, end)] + \
           [f"{word.upper()}{year}" for year in range(start, end)]

def generate_wordlist(words, combination_type, count):
    clear_screen_with_message("\033[32m\n❯❯❯ Generating wordlist..\033[0m")
    logging.info("Wordlist generation started.")
    time.sleep(5)
    wordlist = set()

    if combination_type == "1":
        for word in words:
            wordlist.update([word + "123", "123" + word, word + "456"])
    elif combination_type == "2":
        for word in words:
            wordlist.update(generate_years_combination(word))
    elif combination_type == "3":
        special_chars = ["!", "@", "#", "$", "%"]
        for word in words:
            for char in special_chars:
                wordlist.add(word + char)
                wordlist.add(word + char + "123")
    elif combination_type == "4":
        for word in words:
            randomized = ''.join(random.choice([c.lower(), c.upper()]) for c in word)
            wordlist.add(randomized + str(random.randint(100, 999)))
    elif combination_type == "5":
        for word in words:
            for year in range(1900, 2025):
                wordlist.update([word + "123", "123" + word,
                                 word.capitalize() + str(year),
                                 word.upper() + str(year),
                                 word + "!", word + "@123",
                                 ''.join(random.choice([c.lower(), c.upper()]) for c in word) + str(random.randint(100, 999))
                                 ])
    
    logging.info(f"Generated {len(wordlist)} combinations.")
    return list(wordlist)[:count]

def save_wordlist(wordlist, filename):
    clear_screen_with_message("\033[32m\n❯❯ Saving wordlist..\033[0m")
    logging.info("Saving wordlist to file.")
    with open(filename, "w", encoding="utf-8") as f:
        for word in wordlist:
            f.write(word + "\n")
    clear_screen_with_message(f"\033[47;30m\n❯❯ Wordlist successfully saved to {os.path.abspath(filename)}\n\033[0m")
    logging.info(f"Wordlist successfully saved to {os.path.abspath(filename)}")
    print("*The notification takes 10 seconds to appear.")
    time.sleep(10)

def main():
    print_header()

    output_file = choose_output_file()

    while True:
        clear_screen_with_message("\033[33m\n❯ Enter words separated by spaces.\033[0m")
        words_input = input("Words: ").split()

        if words_input:
            clear_screen_with_message("\033[32m***Words selected\033[0m")
            time.sleep(2)
            break
        else:
            clear_screen_with_message("\033[31m***Invalid Input. Please enter the words.\033[0m")
            time.sleep(2)

    combination_type = choose_combination_type()

    word_count = ask_wordlist_length()

    wordlist = generate_wordlist(words_input, combination_type, word_count)

    save_wordlist(wordlist, output_file)

    logging.info("Operation completed successfully.")

    clear_screen_with_message("❯ It will automatically shut down after 5 seconds...")
    time.sleep(5)

if __name__ == "__main__":
    main()
