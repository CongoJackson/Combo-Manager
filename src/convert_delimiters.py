import os
from colorama import Fore
from tkinter import Tk, filedialog

def convert_delimiters(file_path=None):
    if not file_path:
        print(Fore.CYAN + "Please choose the combo file to convert delimiters...")
        Tk().withdraw()
        file_path = filedialog.askopenfilename(
            initialdir=os.getcwd(),
            title="Select combo list",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        if not file_path:
            print(Fore.RED + "No file selected, returning to menu.")
            return

    delimiters = {
        "1": ":",
        "2": ";",
        "3": "|",
        "4": ",",
        "5": "\t",
        "6": "-"
    }

    print(Fore.YELLOW + "Choose the delimiter you want to convert TO:")
    for num, delim in delimiters.items():
        display = "\\t (tab)" if delim == "\t" else delim
        print(Fore.GREEN + f"{num}. {display}")
    print(Fore.GREEN + "Or type any other delimiter character you want:")

    choice = input(Fore.CYAN + "Your choice: ").strip()

    if choice in delimiters:
        target_delim = delimiters[choice]
    elif choice == "\\t":
        target_delim = "\t"
    else:
        target_delim = choice

    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            lines = [line.strip() for line in f if line.strip()]
    except Exception as e:
        print(Fore.RED + f"Failed to read the file: {e}")
        return

    delimiter_counts = {d: 0 for d in delimiters.values()}
    for line in lines:
        for d in delimiter_counts.keys():
            delimiter_counts[d] += line.count(d)
    source_delim = max(delimiter_counts, key=delimiter_counts.get)
    if delimiter_counts[source_delim] == 0:
        print(Fore.RED + "Could not detect a common delimiter in the file.")
        return

    if source_delim == target_delim:
        print(Fore.YELLOW + "Source delimiter and target delimiter are the same. No conversion needed.")
        return

    converted_lines = []
    for line in lines:
        parts = line.split(source_delim)
        converted_lines.append(target_delim.join(parts))

    base_name, ext = os.path.splitext(os.path.basename(file_path))
    dir_name = os.path.dirname(file_path)
    output_path = os.path.join(dir_name, f"{base_name}-delimiter-converted{ext}")

    try:
        with open(output_path, "w", encoding="utf-8") as out_f:
            out_f.write("\n".join(converted_lines) + "\n")
    except Exception as e:
        print(Fore.RED + f"Failed to write output file: {e}")
        return

    print(Fore.GREEN + f"✅ Conversion complete!")
    source_display = source_delim if source_delim != '\t' else '\\t'
    target_display = target_delim if target_delim != '\t' else '\\t'

    print(Fore.GREEN + f"Source delimiter detected: '{source_display}'")
    print(Fore.GREEN + f"Target delimiter used: '{target_display}'")
    print(Fore.GREEN + f"Saved converted combos to: {output_path}")
    print(Fore.GREEN + f"Total combos: {len(converted_lines)}")
