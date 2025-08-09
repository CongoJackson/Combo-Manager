import os
from colorama import Fore, Style


def remove_duplicates(file_path):
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            lines = f.read().splitlines()

        print(Fore.CYAN + f"\nLoaded {len(lines)} lines from {os.path.basename(file_path)}")

        unique_lines = list(dict.fromkeys(lines))
        removed_count = len(lines) - len(unique_lines)

        base_name, ext = os.path.splitext(file_path)
        output_path = f"{base_name}-remove-duplicate{ext}"

        with open(output_path, "w", encoding="utf-8") as f:
            f.write("\n".join(unique_lines))

        print(Fore.GREEN + f"✅ Removed {removed_count} duplicates.")
        print(Fore.YELLOW + f"💾 Saved output to: {output_path}")

    except Exception as e:
        print(Fore.RED + f"❌ Error processing file: {e}")
