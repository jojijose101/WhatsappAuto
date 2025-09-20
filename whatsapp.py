import os
import subprocess
import time
import sys      
from typing import List
import csv


try:
    import pyautogui as pag
except Exception:
    pag = None



WELCOME = r"""
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
"""




# Function to send WhatsApp messages to multiple contacts
def read_contacts_from_csv(file_path: str) -> List[str]:
    contact =  []
    print("hi")
    with open(file_path, newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if not row:
                continue
            contact.append(row[0].strip())
    return contact



def send_whatsapp_bulk(contacts: List[str], message: str, headless: bool = False, profile_dir: str = "./whatsapp_profile"):
    if pag is None:
        print("pyautogui is not installed. Please install it to use this feature.")
        return

    
    try:
        subprocess.Popen(["cmd", "/C", "start whatsapp://send?"], shell=True)
        time.sleep(5)
        
        
    except Exception as e:
        print("Failed to start whatsapp. Ensure whatsapp application is installed ")
        print(f"Error initializing WebDriver: {e}")
        subprocess.Popen(["cmd", "/C", "start whatsapp://send?"], shell=True)
        time.sleep(5)
        return

    try:
        

        for name in contacts:
            print(f"Searching chat: '{name}' ...")
            pag.hotkey("ctrl", "f")
            time.sleep(1)
            pag.typewrite(name)
            time.sleep(1)
            pag.press("down")
            time.sleep(1)
            pag.press("enter")
            time.sleep(1)
            pag.typewrite(f"{message}")
            time.sleep(2)
            pag.press("enter")
            time.sleep(1)

            pag.hotkey("ctrl", "f")
            time.sleep(.5)  
            pag.hotkey("ctrl", "a")
            time.sleep(.5)
        print("Done sending to all contacts.")

    finally:
        pag.hotkey("alt", "f4")
        print("Whatsapp closed.")
        

def open_file_dialog(): 
    
    try:
        import tkinter as tk
        from tkinter import filedialog
    except ImportError:
        print("tkinter is not available. Please provide the file path manually.")
        return None
    
    root = tk.Tk()
    root.withdraw() 
     # Hide the root window
    file_path = filedialog.askopenfilename(
        title="Select contacts CSV",
        filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")]
    )
          # Give some time for the dialog to close
    return file_path if file_path else None

def option_whatsapp_flow(): 
    print("\n--- WhatsApp bulk sender ---")
    print("You can provide a CSV file (one contact name per line) or enter names manually.")
    choice = input("Load contacts from CSV? (y/n) [y]: ").strip().lower() or "y"

    if choice == 'y':
        path= open_file_dialog()
        print(path)
        try:
            if not path:
                print("No file selected.")
                return
            contacts = read_contacts_from_csv(path)
            
            if not contacts:
                print("No contacts found in the CSV file.")
                return
        except Exception as e:
            print(f"Error reading CSV file: {e}")
            return

    else:
        contacts_input = input("Enter contact names separated by commas: ").strip()
        contacts = [name.strip() for name in contacts_input.split(',') if name.strip()]
        if not contacts:
            print("No valid contact names entered.")
            return
    message = input("Enter the message to send to all contacts:\n> ")
    headless = False
    send_whatsapp_bulk(contacts, message, headless=headless)

# Function to repeat a message multiple times in any focused application
def message_repeater(name: str, message: str, count: int, in_contact: bool = True, number: str = "", delay: int = 10):
    print(in_contact, number)
    try:
        print(f"You have {delay} seconds to focus the target application/window...") 

        if in_contact:  # Contact saved in WhatsApp
            subprocess.Popen(["cmd", "/C", "start whatsapp://send?"], shell=True)
            time.sleep(delay)
            print(f"Searching chat: '{name}' ...")
            pag.hotkey("ctrl", "f")
            time.sleep(1)
            pag.typewrite(name)
            time.sleep(1)
            pag.press("down")
            time.sleep(1)
            pag.press("enter")
            time.sleep(1)
        else:  # Send using number
            try:
                time.sleep(2)
                subprocess.Popen(
                    ["cmd", "/C", f'start whatsapp://send?phone={number}&text=Hello'],
                    shell=True
                )
                time.sleep(delay)
            except Exception as e:
                print("Entered number is invalid or WhatsApp is not installed.")

        # Send repeated messages
        for _ in range(count):
            time.sleep(0.5)
            pag.typewrite(message)
            time.sleep(0.5)
            pag.press("enter")
            time.sleep(0.5)
    finally:
        pag.hotkey("alt", "f4")
        print("WhatsApp closed.")



def repeat_message():
    if pag is None:
        print("pyautogui is not installed. Please install it to use this feature.")
        return
    contact = input("Is the contact saved in WhatsApp? (y/n) [n]: ").strip().lower() or "y"
    in_contact = True
    if contact == 'y':
        in_contact = True
        name = input("Enter the name you want to send message: ")
        number = ""
    else:  
        name = ""
        in_contact = False
        number = input("Enter the phone number with country code (e.g., +911234567890): ")
        

    print("\n--- Repeat Message ---")
    message = input("Enter the message to repeat: ")
    try:
        count = int(input("Enter the number of times to repeat the message: "))
    except ValueError:
        print("Invalid number. Please enter an integer.")
        return
    try:
        message_repeater(name, message, count, in_contact, number)
    except KeyboardInterrupt:
        print("\nMessage repeating interrupted by user.")   

    


def main():
    print(WELCOME)
    choice = input("Enter your choice (1/2/0): ")
    
    if choice == '1':
        option_whatsapp_flow()
    elif choice == '2':
        repeat_message()
        
    elif choice == '0':
        print("Exiting the program. Goodbye!")
        sys.exit()
    elif choice == "3":
        open_file_dialog()
    else:
        print("Invalid choice. Please try again.")
        main()  

if __name__ == "__main__":
    main()