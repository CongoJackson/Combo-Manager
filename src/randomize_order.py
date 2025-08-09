import os
import random
from colorama import Fore
from tkinter import Tk, filedialog

def randomize_order(file_path=None):
    if not file_path:
        print(Fore.CYAN + "Please choose the combo file to randomize...")
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
            lines = [line.strip() for line in f if line.strip()]
    except Exception as e:
        print(Fore.RED + f"Failed to read the file: {e}")
        return

    random.shuffle(lines)

    base_name, ext = os.path.splitext(os.path.basename(file_path))
    dir_name = os.path.dirname(file_path)
    output_path = os.path.join(dir_name, f"{base_name}-randomized{ext}")

    try:
        with open(output_path, "w", encoding="utf-8") as out_f:
            out_f.write("\n".join(lines) + "\n")
    except Exception as e:
        print(Fore.RED + f"Failed to write output file: {e}")
        return

    print(Fore.GREEN + f"✅ Randomization complete!")
    print(Fore.GREEN + f"Saved randomized combos to: {output_path}")
    print(Fore.GREEN + f"Total combos: {len(lines)}")
