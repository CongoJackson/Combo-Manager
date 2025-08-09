import os
from colorama import Fore
from tkinter import Tk, filedialog

def validate_format(file_path=None):
    if not file_path:
        print(Fore.CYAN + "Please choose the combo file to validate...")
        Tk().withdraw()
        file_path = filedialog.askopenfilename(
            initialdir=os.getcwd(),
            title="Select combo list",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        if not file_path:
            print(Fore.RED + "No file selected, returning to menu.")
            return

    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            lines = f.readlines()
    except Exception as e:
        print(Fore.RED + f"Failed to read the file: {e}")
        return

    seen = set()
    valid_lines = []
    removed_count = 0

    for line in lines:
        line = line.strip()
        if line.count(":") == 1 and line not in seen:
            valid_lines.append(line)
            seen.add(line)
        else:
            removed_count += 1

    base_name, ext = os.path.splitext(os.path.basename(file_path))
    dir_name = os.path.dirname(file_path)
    output_path = os.path.join(dir_name, f"{base_name}-validated{ext}")

    try:
        with open(output_path, "w", encoding="utf-8") as out_f:
            out_f.write("\n".join(valid_lines) + "\n")
    except Exception as e:
        print(Fore.RED + f"Failed to write output file: {e}")
        return

    print(Fore.GREEN + f"✅ Validation complete! Removed {removed_count} invalid or duplicate lines.")
    print(Fore.GREEN + f"Saved valid combos to: {output_path}")
    print(Fore.GREEN + f"Total valid combos: {len(valid_lines)}")
    print(Fore.GREEN + f"Removed {removed_count} Invalid combos")
