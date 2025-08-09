import os
import sys
import tkinter as tk
from tkinter import filedialog
from colorama import Fore, Style, init
from src.remove_duplicates import remove_duplicates
from src.extract_emails import extract_emails
from src.provider_sorter import provider_sorter
from src.split import split_combos
from src.merge import merge_files
from src.validate_format import validate_format
from src.randomize_order import randomize_order
from src.convert_delimiters import convert_delimiters
from src.extract_only_usernames import extract_only_usernames
from src.extract_only_passwords import extract_only_passwords
from src.extract_user_from_email import extract_user_from_email

init(autoreset=True)


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def main_menu():
    tasks = {
        "1": ("Remove duplicates", remove_duplicates),
        "2": ("Extract emails", extract_emails),
        "3": ("Provider sorter", provider_sorter),
        "4": ("Split Combos List", split_combos),
        "5": ("Merge combo lists", merge_files),
        "6": ("Validate Combo Format", validate_format),
        "7": ("Randomize combo order", randomize_order),
        "8": ("Convert delimiters", convert_delimiters),
        "9": ("Extract only usernames", extract_only_usernames),
        "10": ("Extract only passwords", extract_only_passwords),
        "11": ("Extract User from Email", extract_user_from_email),
        "0": ("Exit", None)
    }


    while True:
        clear_screen()
        print(Fore.CYAN + Style.BRIGHT + "=== Combo List Manager ===\n")
        for key, (name, _) in tasks.items():
            print(Fore.LIGHTCYAN_EX + f"{key}. {name}")

        choice = input(Fore.GREEN + "\nSelect a task: ").strip()

        if choice not in tasks:
            print(Fore.RED + "Invalid choice. Press Enter to try again...")
            input()
            continue

        if choice == "0":
            print(Fore.MAGENTA + "Goodbye! 👋")
            sys.exit(0)

        task_name, task_func = tasks[choice]
        print(Fore.CYAN + f"\nSelected: {task_name}")
        print(Fore.YELLOW + "Please choose the file...")

        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename(
            initialdir=os.getcwd(),
            title="Select combo list",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )

        if not file_path:
            print(Fore.RED + "No file selected. Returning to menu...")
            input(Fore.GREEN + "Press Enter to continue...")
            continue

        task_func(file_path)

        print(Fore.CYAN + "\nTask completed.")
        print(Fore.YELLOW + "1. Perform another task")
        print(Fore.YELLOW + "0. Exit")

        sub_choice = input(Fore.GREEN + "\nSelect an option: ").strip()
        if sub_choice == "0":
            print(Fore.MAGENTA + "Goodbye! 👋")
            sys.exit(0)


if __name__ == "__main__":
    main_menu()
