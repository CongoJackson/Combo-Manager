import os
from tkinter import Tk, filedialog
from colorama import Fore

def extract_only_usernames(file_path=None):
    print(Fore.CYAN + "Please choose the combo file to extract usernames from..." if not file_path else "")
    if not file_path:
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

    total_lines = len(lines)
    usernames = set()

    for line in lines:
        line = line.strip()
        if ':' in line:
            username = line.split(':', 1)[0]
            usernames.add(username)
        else:
            usernames.add(line)

    unique_count = len(usernames)

    base_name = os.path.splitext(os.path.basename(file_path))[0]
    dir_name = os.path.dirname(file_path)
    output_path = os.path.join(dir_name, f"{base_name}-onlyusernames.txt")

    try:
        with open(output_path, "w", encoding="utf-8") as out_f:
            for username in usernames:
                out_f.write(username + "\n")
    except Exception as e:
        print(Fore.RED + f"Failed to write output file: {e}")
        return

    print(Fore.GREEN + f"Total lines processed: {total_lines}")
    print(Fore.GREEN + f"Unique usernames extracted: {unique_count}")
    print(Fore.GREEN + f"Saved to: {output_path}")
