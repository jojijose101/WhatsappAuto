# WhatsappAuto
# 🔥 Auto-Messenger Terminal Tool 🔥

A simple Python-based automation tool to send or repeat WhatsApp messages.  
Built with **pyautogui**, **subprocess**, and **tkinter**.

---

## 📌 Features
- ✅ Send bulk messages to multiple WhatsApp contacts (via CSV or manual input)  
- ✅ Repeat a message multiple times in any focused WhatsApp chat or app  
- ✅ Import contacts via CSV file dialog (`tkinter`)  
- ✅ Automate repetitive messaging tasks with ease  

---

## 🖥️ Demo

 ╔══════════════════════════════════════════════════════════╗
║                                                          ║
║      █████╗ ██╗   ██╗████████╗ ██████╗      ███╗   ███╗  ║
║     ██╔══██╗██║   ██║╚══██╔══╝██╔═══██╗     ████╗ ████║  ║
║     ███████║██║   ██║   ██║   ██║   ██║     ██╔████╔██║  ║
║     ██╔══██║██║   ██║   ██║   ██║   ██║     ██║╚██╔╝██║  ║
║     ██║  ██║╚██████╔╝   ██║   ╚██████╔╝     ██║ ╚═╝ ██║  ║
║     ╚═╝  ╚═╝ ╚═════╝    ╚═╝    ╚═════╝      ╚═╝     ╚═╝  ║
║                                                          ║
║              🔥  AUTO-MESSENGER TERMINAL TOOL  🔥        ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝

        ===========================================
           Welcome to Simple Mass Messenger Tool
                     Created by Joji
        ===========================================
        Choose an option:
         1) Message to multiple members (WhatsApp Web)
         2) Repeat message many times (any focused app/window)
         0) Exit
        ===========================================


---

## ⚙️ Installation

```bash
git clone https://github.com/jojijose/auto-messenger-tool.git
cd auto-messenger-tool

# Create virtual environment (optional but recommended)
python -m venv venv

# Activate virtual environment
# On Linux/Mac:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

## Requirements

pyautogui
tkinter     # included in most Python installations
csv         # standard Python library
subprocess  # standard Python library
time        # standard Python library
sys         # standard Python library
os          # standard Python library

## USAGE

```bash
$ python messenger.py

##  Menu Options:

[1] Send WhatsApp messages to multiple contacts
[2] Repeat a message many times
[0] Exit


## EXAMPLE CSV (contacts.csv)

Alice
Bob
Charlie

## NOTES:

⚠️ Keep WhatsApp Desktop open and logged in

⚠️ Do not touch mouse/keyboard while automation is running

⚠️ Adjust timing (time.sleep) if needed for your system

## AUTHOR

👨‍💻 Joji Jose
GitHub: https://github.com/yourusername

