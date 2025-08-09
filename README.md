# 🔐 Combo Manager

[![Python](https://img.shields.io/badge/Python-3.6%2B-blue.svg)](https://python.org)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)

A powerful and user-friendly command-line tool for managing email:password combination lists. This tool provides a comprehensive suite of utilities for processing, cleaning, and organizing credential lists with an intuitive menu-driven interface.

## ✨ Features

### 🛠 Core Tools

- **🗑 Remove Duplicates** - Efficiently removes duplicate entries while preserving order
- **📧 Extract Emails** - Extracts all valid email addresses using regex pattern matching
- **🏢 Provider Sorter** - Sorts and filters combos by email provider domains with detailed statistics
- **✂️ Split Combos** - Splits large combo files into smaller, manageable chunks
- **🔗 Merge Files** - Combines multiple combo files into a single unified list
- **✅ Validate Format** - Ensures all entries follow the correct username:password format
- **🔀 Randomize Order** - Randomizes the order of entries for better distribution
- **🔄 Convert Delimiters** - Converts between different delimiter formats (e.g., : to |)
- **👤 Extract Usernames** - Extracts only the username portion from combos
- **🔑 Extract Passwords** - Extracts only the password portion from combos
- **📨 Extract User from Email** - Extracts username part from email addresses

### 🎨 User Experience

- **Interactive GUI** - File selection dialogs for easy navigation
- **Colorful Output** - Terminal output with colors for better readability
- **Progress Feedback** - Real-time statistics and operation results
- **Error Handling** - Robust error handling with informative messages
- **Cross-Platform** - Works on Windows, Linux, and macOS

## 🚀 Installation

### Prerequisites

Make sure you have Python 3.6+ installed on your system.

### Required Dependencies

Install the required packages using pip:

```bash
pip install -r requirements.txt
```

Or install manually:
```bash
pip install colorama
```

### Quick Start

1. Clone or download this repository
2. Navigate to the project directory
3. Install dependencies: `pip install -r requirements.txt`
4. Run the main script:

```bash
python main.py
```

## 📖 Usage

Launch the application by running `python main.py`. You'll see an interactive menu with numbered options:

```
=== Combo List Manager ===

1. Remove duplicates
2. Extract emails
3. Provider sorter
4. Split Combos List
5. Merge combo lists
6. Validate Combo Format
7. Randomize combo order
8. Convert delimiters
9. Extract only usernames
10. Extract only passwords
11. Extract User from Email
0. Exit
```

Simply enter the number corresponding to your desired operation and follow the prompts.

### Input File Format

The tool works with text files containing credentials in the format:
```
username:password
email@domain.com:password123
user@example.org:mypassword
```

## 🎯 Output Files

All processed files are automatically saved with descriptive suffixes:
- `filename-remove-duplicate.txt`
- `filename-extract-emails.txt`  
- `filename-provider-extract-[domains].txt`
- `filename-splitted/` (folder with parts)
- `merged.txt` or `merged-N.txt`
- `filename-validated.txt`
- And more based on the operation performed

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## ⚠️ Disclaimer

This tool is designed for legitimate security research, penetration testing, and educational purposes only. Users are responsible for ensuring compliance with applicable laws and regulations. The authors are not responsible for any misuse of this software.

## 🔍 Security Note

Always handle credential lists responsibly and ensure proper security measures when working with sensitive data. Consider encrypting files when not in use and following your organization's data handling policies.

---

⭐ **Star this repository if you find it useful!**