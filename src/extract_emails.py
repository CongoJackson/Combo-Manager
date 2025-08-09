import os
import re
from colorama import Fore


EMAIL_REGEX = re.compile(
    r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
)


def extract_emails(file_path):
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()

        emails = EMAIL_REGEX.findall(content)
        unique_emails = list(dict.fromkeys(emails))

        print(Fore.CYAN + f"\nFound {len(emails)} emails, {len(unique_emails)} unique.")

        base_name, ext = os.path.splitext(file_path)
        output_path = f"{base_name}-extract-emails{ext}"

        with open(output_path, "w", encoding="utf-8") as f:
            f.write("\n".join(unique_emails))

        print(Fore.GREEN + f"✅ Extracted emails saved to: {output_path}")

    except Exception as e:
        print(Fore.RED + f"❌ Error processing file: {e}")
