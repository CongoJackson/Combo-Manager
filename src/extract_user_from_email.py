import os
from tkinter import Tk, filedialog
from colorama import Fore

def extract_user_from_email(file_path=None):
    if not file_path:
        print(Fore.CYAN + "Please choose the combo file to extract usernames from emails...")
        Tk().withdraw()
        file_path = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select combo file")
        if not file_path:
            print(Fore.RED + "No file selected, returning to menu.")
            return

    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            lines = f.readlines()
    except Exception as e:
        print(Fore.RED + f"Failed to read the file: {e}")
        return

    extracted_users = set()
    total_lines = len(lines)
    invalid_lines = 0

    for line in lines:
        line = line.strip()
        if '@' in line:
            user_part = line.split('@')[0]
            if user_part:
                extracted_users.add(user_part)
            else:
                invalid_lines += 1
        else:
            invalid_lines += 1

    base_name = os.path.splitext(os.path.basename(file_path))[0]
    output_path = os.path.join(os.path.dirname(file_path), f"{base_name}-user-from-email.txt")

    try:
        with open(output_path, "w", encoding="utf-8") as out_f:
            for user in extracted_users:
                out_f.write(user + "\n")
    except Exception as e:
        print(Fore.RED + f"Failed to write output file: {e}")
        return

    print(Fore.GREEN + f"Total lines in file: {total_lines}")
    print(Fore.GREEN + f"Extracted unique usernames: {len(extracted_users)}")
    if invalid_lines > 0:
        print(Fore.YELLOW + f"Skipped {invalid_lines} invalid lines without '@'.")

    print(Fore.GREEN + f"✅ Output saved: {output_path}")
