from datetime import date
import itertools
import logging
import os
import random
import string
import sys

# from memory_profiler import profile, memory_usage  # Keep for easy memory testing later

logging.basicConfig(filename="wordgen.log", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")


def print_brg(message):
    print("\033[32m")
    print(message)
    print("\033[0m")


def print_header():
    print(r"""

░██╗░░░░░░░██╗░█████╗░██████╗░██████╗░░██████╗░███████╗███╗░░██╗
░██║░░██╗░░██║██╔══██╗██╔══██╗██╔══██╗██╔════╝░██╔════╝████╗░██║
░╚██╗████╗██╔╝██║░░██║██████╔╝██║░░██║██║░░██╗░█████╗░░██╔██╗██║
░░████╔═████║░██║░░██║██╔══██╗██║░░██║██║░░╚██╗██╔══╝░░██║╚████║
░░╚██╔╝░╚██╔╝░╚█████╔╝██║░░██║██████╔╝╚██████╔╝███████╗██║░╚███║
░░░╚═╝░░░╚═╝░░░╚════╝░╚═╝░░╚═╝╚═════╝░░╚═════╝░╚══════╝╚═╝░░╚══╝
          """)
    print("\033[0m")
    print(r"""
created by: https://github.com/brgkdm edited by: https://github.com/sudoAshroom
          """)
    print("*If you create the same file twice, it will overwrite the file.")


def choose_output_file():  # dictates file name
    default_name = f"wordlist_{random.randrange(1, 10000000000)}.txt"
    print(f"❯ Default file name: {default_name}\n\nEnter file name (or press Enter for default): ")
    filename = input().strip()
    filename = filename if filename else default_name
    if not filename.endswith(".txt"):
        filename += ".txt"
    print(f"\n***The wordlist will be saved as: {filename} in the current directory.\n")
    return filename


def choose_combination_type():  # Generation choices for the user
    choices = {
        '1': "Words + Numbers (e.g., word123, 123word)",
        '2': "Capitalized + Year (e.g., Word2024)",
        '3': "Words + Special Characters (e.g., word!@#)",
        '4': "Mixed Case Randomized",
        '5': "All Options Combined"
    }
    while True:
        print("❯ Select the type of password combination to generate.")
        for key, value in choices.items():
            print(f"{key}. {value}")
        choice = input("\n❯ Enter your choice (1-5)?: ").strip()
        if choice in choices:
            print(f"\n***{choices[choice]} selected\n")
            return choice
        else:
            print("\n***Invalid choice. Please select a number between 1 and 5.\n")


def ask_wordlist_length():  # Asks user desired amount of generated words
    print("\n❯ How many words (max 1,000,000) do you want to generate?")
    while True:
        try:
            count = int(input("\n❯ Number of words: ").strip())
            if 1 <= count <= 1000000:
                return count
            else:
                print("\n***Please enter a number between 1 and 1,000,000.\n")
        except ValueError:
            print("\n***Please enter a valid number.\n")


def generate_years_combination(word, start=1900, end=None):
    if end is None:
        end = date.today().year
    return [f"{word.capitalize()}{year}" for year in range(start, end)] + \
           [f"{word.upper()}{year}" for year in range(start, end)]


def generate_wordlist(words, combination_type, count):
    print("\n❯❯❯ Generating wordlist...\n")
    logging.info("Wordlist generation started.")
    wordlist = set()

    if combination_type == "1":
        while len(wordlist) < count:
            for word in words:
                wordlist.add(word + ''.join(random.choices(string.digits, k=random.randint(2, 5))))
                if len(wordlist) >= count:
                    break
    elif combination_type == "2":
        for word in words:
            wordlist.update(generate_years_combination(word))
    elif combination_type == "3":
        special_chars = "!@#$%"
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
            for year in range(1900, date.today().year + 1):
                wordlist.update([
                    word + "123", "123" + word,
                    word.capitalize() + str(year),
                    word.upper() + str(year),
                    word + "!", word + "@123",
                    ''.join(random.choice([c.lower(), c.upper()]) for c in word) + str(random.randint(100, 999))
                ])
    logging.info(f"Generated {len(wordlist)} combinations.")
    return list(wordlist)[:count]


def save_wordlist(wordlist, filename):
    print("\n❯❯ Saving wordlist..")
    logging.info("Saving wordlist to file.")
    with open(filename, "w", encoding="utf-8") as f:
        for word in wordlist:
            f.write(word + "\n")
    print(f"\n❯❯ Wordlist successfully saved to {os.path.abspath(filename)}\n")
    logging.info(f"Wordlist successfully saved to {os.path.abspath(filename)}")


def main():
    while True:
        print_header()
        start = input("\033[0m\nPress Enter to start or type anything to quit.\n")
        if start.strip():
            print("\nProgram Closing.\n")
            break
        else:
            output_file = choose_output_file()
            while True:
                print("\n❯ Enter words separated by spaces.")
                words_input = input("Words: ").split()
                if words_input:
                    print("\n***Words selected")
                    break
                else:
                    print("\n***Invalid Input. Please enter the words.")
            combination_type = choose_combination_type()
            word_count = ask_wordlist_length()
            wordlist = generate_wordlist(words_input, combination_type, word_count)
            save_wordlist(wordlist, output_file)
            logging.info("Operation completed successfully.")
            print("Operation complete. Program closing.")
            return


if __name__ == "__main__":
    main()
