import os
import re
from collections import Counter
from colorama import Fore, Style

EMAIL_REGEX = re.compile(
    r"[a-zA-Z0-9_.+-]+@([a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)"
)

def provider_sorter(file_path):
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            lines = f.read().splitlines()

        providers = []
        line_to_provider = []

        for line in lines:
            match = EMAIL_REGEX.search(line)
            if match:
                domain = match.group(1).lower()
                providers.append(domain)
                line_to_provider.append((line, domain))

        if not providers:
            print(Fore.RED + "No valid emails found in file.")
            return

        counts = Counter(providers)
        total_providers = len(counts)

        print(Fore.CYAN + f"\nTotal unique providers found: {total_providers}\n")

        top25 = counts.most_common(25)

        print(Fore.YELLOW + "Top 25 providers:")
        for i, (provider, count) in enumerate(top25, 1):
            print(f"{Fore.GREEN}{i}. {Fore.YELLOW}{provider} - {count}")

        while True:
            print()
            print(Fore.CYAN + "Options:")
            print(Fore.YELLOW + "Enter provider numbers separated by commas to extract combos (e.g., 1,3,5)")
            print(Fore.YELLOW + "B - Back to menu")
            print(Fore.YELLOW + "0 - Exit")

            while True:
                choice = input(Fore.GREEN + "\nYour choice: ").strip().lower()

                if choice == "b":
                    return
                if choice == "0":
                    print(Fore.MAGENTA + "Goodbye! 👋")
                    exit(0)

                try:
                    selected_nums = [int(x) for x in choice.split(",") if x.strip().isdigit()]
                except Exception:
                    print(Fore.RED + "Invalid input. Please enter numbers separated by commas, B, or 0.")
                    continue

                if not selected_nums:
                    print(Fore.RED + "No valid provider numbers selected.")
                    continue

                selected_providers = []
                invalid_nums = []
                for num in selected_nums:
                    if 1 <= num <= len(top25):
                        selected_providers.append(top25[num - 1][0])
                    else:
                        invalid_nums.append(num)

                if invalid_nums:
                    print(
                        Fore.RED + f"Number(s) {', '.join(map(str, invalid_nums))} are out of range. Choose between 1 and {len(top25)}.")
                    continue

                if not selected_providers:
                    print(Fore.RED + "No valid providers selected after filtering.")
                    continue

                extracted_lines = [
                    line for line, domain in line_to_provider if domain in selected_providers
                ]

                if not extracted_lines:
                    print(Fore.RED + "No combos found for selected providers.")
                    continue

                base_name, ext = os.path.splitext(file_path)
                providers_str = "-".join([p.replace(".", "_") for p in selected_providers])
                output_path = f"{base_name}-provider-extract-{providers_str}{ext}"

                with open(output_path, "w", encoding="utf-8") as f:
                    f.write("\n".join(extracted_lines))

                print(Fore.GREEN + f"✅ Extracted {len(extracted_lines)} combos to {output_path}")

                while True:
                    next_action = input(
                        Fore.CYAN + "\nExtract more providers? (Y)es / (N)o to return to menu: ").strip().lower()
                    if next_action == "y":
                        break
                    elif next_action == "n":
                        return
                    else:
                        print(Fore.RED + "Please type Y or N.")

    except Exception as e:
        print(Fore.RED + f"❌ Error processing file: {e}")
