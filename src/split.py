import os
from colorama import Fore
from tkinter import Tk, filedialog

def split_combos():
    print(Fore.CYAN + "Please choose the combo file to split...")
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
    print(Fore.GREEN + f"Total lines in file: {total_lines}")

    while True:
        per_file_str = input(Fore.YELLOW + "How many lines per split file? (e.g., 1000): ").strip()
        if per_file_str.isdigit() and int(per_file_str) > 0:
            lines_per_file = int(per_file_str)
            break
        else:
            print(Fore.RED + "Please enter a valid positive integer.")

    base_name = os.path.splitext(os.path.basename(file_path))[0]
    dir_name = os.path.dirname(file_path)
    output_folder = os.path.join(dir_name, f"{base_name}-splitted")

    os.makedirs(output_folder, exist_ok=True)

    file_count = 0
    for i in range(0, total_lines, lines_per_file):
        file_count += 1
        part_lines = lines[i:i + lines_per_file]
        output_path = os.path.join(output_folder, f"{base_name}-part{file_count}.txt")
        try:
            with open(output_path, "w", encoding="utf-8") as out_f:
                out_f.writelines(part_lines)
        except Exception as e:
            print(Fore.RED + f"Failed to write part {file_count}: {e}")
            return

    print(Fore.GREEN + f"✅ File split into {file_count} parts in folder: {output_folder}")
