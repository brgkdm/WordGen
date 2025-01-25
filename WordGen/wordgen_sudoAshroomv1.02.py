import itertools
import random
import string
import os
import sys
import logging
import random
from datetime import date

#from memory_profiler import profile, memory_usage            #Keep for easy memory testing later



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

def choose_output_file():                                  #dictates file name
    default_name = f"wordlist_{random.randrange(1,10000000000)}.txt"
    print(f"❯ Default file name: {default_name}\n\nEnter file name (or press Enter for default): ")
    filename = input()
    if not filename:
        filename = default_name
    if not filename.endswith(".txt"):
        filename += ".txt"
    print(f"\n***The wordlist will be saved as: {filename} in the current directory.\n")
    return filename

def choose_combination_type():                             #Generation choices for the user
    while True:
        print("❯ Select the type of password combination to generate.\n\n1. Words + Numbers (e.g., word123, 123word)\n2. Capitalized + Year (e.g., Word2024)\n3. Words + Special Characters (e.g., word!, word@123)\n4. Mixed Case Randomized (e.g., wOrD123)\n5. All Options Combined (recommended)")
        choice = input("\n❯ Enter your choice (1-5)?: ").strip() #strip to catch an accidental space in input

        if choice == '1':
            print("\n***Words + Numbers selected\n")
            return choice
        elif choice == '2':
            print("\n***Capitalized + Year selected\n")
            return choice
        elif choice == '3':
            print("\n***Words + Special Characters selected\n")
            return choice
        elif choice == '4':
            print("\n***Mixed Case Randomized selected\n")
            return choice
        elif choice == '5':
            print("\n***All Options Combined selected\n")
            return choice
        else:
            print("\n***Invalid choice. Please select a number between 1 and 5.\n")

def ask_wordlist_length():                                #Asks user desired amount of generated words
    print("\n❯ How many words (max 1.000.000) do you want to generate?")
    while True:
        try:
            count = (input("\n❯ Number of words: ")).strip()   #strip to catch an accidental space in input
            if 1 <= int(count) <= 1000000:
                return count
            else:
                print("\n***Please enter a number between 1 and 1.000.000.\n")
        except ValueError:
            print("\n***Please enter a number between 1 and 1.000.000\n")

def generate_years_combination(word, start=1900, end=str(date.today().strftime("%Y"))):       #calling current year instead of a set year
    return [f"{word.capitalize()}{year}" for year in range(int(start), int(end))] + \
           [f"{word.upper()}{year}" for year in range(int(start), int(end))]


#WORD GENERATION
def generate_wordlist(words, combination_type, count):
    print("\n❯❯❯ Generating wordlist...\n")
    logging.info("Wordlist generation started.")
    wordlist = set()

    if combination_type == "1":
        count1 = 0
        while count1 != int(count):          #Using a while loop instead of 'for word in words' to ensure we can go for the desired count, even if that's greater than numbers provided
            word = words[count1 % len(words)]      #This loops the list if desired word count is higher than input word count
            wordlist.update([word + ''.join(str(random.randint(0, 9)) for _ in range(random.randint(2, 5)))])   #Uses random to generate a number between 0-9, and a random amount between 2 and 5. This generates outcomes between 00-99999
            count1 += 1
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
    return list(wordlist)[:int(count)]


#WORD WRITING
def save_wordlist(wordlist, filename):
    print("\n❯❯ Saving wordlist..")
    logging.info("Saving wordlist to file.")
    with open(filename, "w", encoding="utf-8") as f:
        for word in wordlist:
            f.write(word + "\n")
    print(f"\n❯❯ Wordlist successfully saved to {os.path.abspath(filename)}\n")
    logging.info(f"Wordlist successfully saved to {os.path.abspath(filename)}")
    print("*The notification takes 10 seconds to appear.")


#@profile #memory testing                            #Keep for easy memory testing later
def main():
    while True:
        print_header()
        start = input("\033[0m\nPress Enter to start or type anything to quit.\n")
        if start != "":
            break
        elif start == "":
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

            print("❯ It will automatically shut down after 5 seconds...")
            return

main()

