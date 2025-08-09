import os
from tkinter import Tk, filedialog
from colorama import Fore

def merge_files():
    print(Fore.CYAN + "Please select one or more files to merge...")
    Tk().withdraw()
    file_paths = filedialog.askopenfilenames(
        initialdir=os.getcwd(),
        title="Select combo files to merge",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )

    if not file_paths:
        print(Fore.RED + "No files selected, returning to menu.")
        return

    base_dir = os.path.dirname(file_paths[0])
    base_name = "merged"
    ext = ".txt"

    output_path = os.path.join(base_dir, base_name + ext)
    counter = 1
    while os.path.exists(output_path):
        output_path = os.path.join(base_dir, f"{base_name}-{counter}{ext}")
        counter += 1

    total_lines = 0
    try:
        with open(output_path, "w", encoding="utf-8") as out_f:
            for file_path in file_paths:
                with open(file_path, "r", encoding="utf-8", errors="ignore") as in_f:
                    lines = in_f.readlines()
                    total_lines += len(lines)
                    out_f.writelines(lines)
    except Exception as e:
        print(Fore.RED + f"Failed to merge files: {e}")
        return

    print(Fore.GREEN + f"✅ Files merged into: {output_path}")
    print(Fore.GREEN + f"Total lines in merged file: {total_lines}")
