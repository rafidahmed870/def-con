#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════╗
║       Windows Defender Controller            ║
║       Developed By : Rafid                   ║
╚══════════════════════════════════════════════╝
"""

import os
import sys
import ctypes
import shutil
import winreg

class C:
    RED     = "\033[91m"
    GREEN   = "\033[92m"
    YELLOW  = "\033[93m"
    BLUE    = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN    = "\033[96m"
    WHITE   = "\033[97m"
    BOLD    = "\033[1m"
    DIM     = "\033[2m"
    RESET   = "\033[0m"

def print_text(text: str, color: str = C.WHITE, indent: int = 0):
    print(f"{indent * ' '}{color}{text}{C.RESET}")

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def progress_bar(progress: int, total: int, prefix: str = "", suffix: str = "", length: int = 50):
    percent = ("{0:.1f}").format(100 * (progress / float(total)))
    filled_length = int(length * progress // total)
    bar = f"{C.GREEN}{'█' * filled_length}{C.RESET}{C.DIM}{'-' * (length - filled_length)}{C.RESET}"
    colored_line = f"{C.CYAN}{prefix}{C.RESET} |{bar}| {C.YELLOW}{percent}%{C.RESET} {suffix}"
    # Create a plain text version for calculating line length (without ANSI codes)
    plain_line = f"{prefix} |{'█' * filled_length}{'-' * (length - filled_length)}| {percent}% {suffix}"
    # Clear the line completely first, then print the new line
    sys.stdout.write("\r\033[2K") 
    print(f"\r{' ' * len(plain_line):<{len(plain_line)}}", end="\r")
    print(f"\r{colored_line}", end="\r")
    if progress == total:
        print()

def is_admin() -> bool:
    try:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0
    except Exception:
        return False
    
def def_con(enable: bool) -> bool:
    if not is_admin():
        print_text("Please run this script as Administrator.", C.RED, 2)
        return False

    def_path1 = r"SOFTWARE\Policies\Microsoft\Windows Defender"
    def_path2 = r"SOFTWARE\Policies\Microsoft\Windows Defender\Real-Time Protection"
    def_path3 = r"SOFTWARE\Policies\Microsoft\Windows Defender\Signature Update"
    def_path4 = r"SOFTWARE\Policies\Microsoft\Windows Defender\Spynet"

    status = "Enabling" if enable else "Disabling"
    total_steps = 13  # 5 + 3 + 1 + 1 + 3 (close keys)
    
    try:
        progress_bar(1, total_steps, f"{status} Windows Defender", "Creating registry keys")
        
        # Create or open registry keys with write access
        key1 = winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, def_path1)
        key2 = winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, def_path2)
        key3 = winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, def_path3)
        key4 = winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, def_path4)
        
        progress_bar(2, total_steps, f"{status} Windows Defender", "Updating main settings")
        
        if enable:
            winreg.SetValueEx(key1, "DisableAntiSpyware", 0, winreg.REG_DWORD, 0)
            winreg.SetValueEx(key1, "DisableAntiVirus", 0, winreg.REG_DWORD, 0)
            winreg.SetValueEx(key1, "DisableSpecialRunningModes", 0, winreg.REG_DWORD, 0)
            winreg.SetValueEx(key1, "DisableRoutinelyTakingAction", 0, winreg.REG_DWORD, 0)
            winreg.SetValueEx(key1, "ServiceKeepAlive", 0, winreg.REG_DWORD, 0)
            
            progress_bar(7, total_steps, f"{status} Windows Defender", "Updating real-time settings")
            
            winreg.SetValueEx(key2, "DisablebehaviourMonitoring", 0, winreg.REG_DWORD, 0)
            winreg.SetValueEx(key2, "DisableOnAccessProtection", 0, winreg.REG_DWORD, 0)
            winreg.SetValueEx(key2, "DisableRealtimeMonitoring", 0, winreg.REG_DWORD, 0)
            
            progress_bar(10, total_steps, f"{status} Windows Defender", "Updating update settings")
            
            winreg.SetValueEx(key3, "ForceUpdateFromMU", 0, winreg.REG_DWORD, 0)
            
            progress_bar(11, total_steps, f"{status} Windows Defender", "Updating spynet settings")
            
            winreg.SetValueEx(key4, "DisableBlockAtFirstSeen", 0, winreg.REG_DWORD, 0)
        else:
            winreg.SetValueEx(key1, "DisableAntiSpyware", 0, winreg.REG_DWORD, 1)
            winreg.SetValueEx(key1, "DisableAntiVirus", 0, winreg.REG_DWORD, 1)
            winreg.SetValueEx(key1, "DisableSpecialRunningModes", 0, winreg.REG_DWORD, 1)
            winreg.SetValueEx(key1, "DisableRoutinelyTakingAction", 0, winreg.REG_DWORD, 1)
            winreg.SetValueEx(key1, "ServiceKeepAlive", 0, winreg.REG_DWORD, 1)
            
            progress_bar(7, total_steps, f"{status} Windows Defender", "Updating real-time settings")
            
            winreg.SetValueEx(key2, "DisablebehaviourMonitoring", 0, winreg.REG_DWORD, 1)
            winreg.SetValueEx(key2, "DisableOnAccessProtection", 0, winreg.REG_DWORD, 1)
            winreg.SetValueEx(key2, "DisableRealtimeMonitoring", 0, winreg.REG_DWORD, 1)
            
            progress_bar(10, total_steps, f"{status} Windows Defender", "Updating update settings")
            
            winreg.SetValueEx(key3, "ForceUpdateFromMU", 0, winreg.REG_DWORD, 1)
            
            progress_bar(11, total_steps, f"{status} Windows Defender", "Updating spynet settings")
            
            winreg.SetValueEx(key4, "DisableBlockAtFirstSeen", 0, winreg.REG_DWORD, 1)
        
        progress_bar(12, total_steps, f"{status} Windows Defender", "Closing registry keys")
        
        # Close the keys
        winreg.CloseKey(key1)
        winreg.CloseKey(key2)
        winreg.CloseKey(key3)
        winreg.CloseKey(key4)
        
        progress_bar(13, total_steps, f"{status} Windows Defender", "Completed!")
        
        return True
    except Exception as e:
        print_text(f"\nError: {e}", C.RED, 2)
        return False
    
def update_con(enable: bool) -> bool:
    if not is_admin():
        print_text("Please run this script as Administrator.", C.RED, 2)
        return False
    
    update_path = r"SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\AU"
    
    status = "Enabling" if enable else "Disabling"
    total_steps = 4
    
    try:
        progress_bar(1, total_steps, f"{status} Windows Update", "Creating registry key")
        
        key = winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, update_path)
        
        progress_bar(2, total_steps, f"{status} Windows Update", "Updating settings")
        
        if enable:
            winreg.SetValueEx(key, "NoAutoUpdate", 0, winreg.REG_DWORD, 0)
        else:
            winreg.SetValueEx(key, "NoAutoUpdate", 0, winreg.REG_DWORD, 1)
        
        progress_bar(3, total_steps, f"{status} Windows Update", "Closing registry key")
        
        winreg.CloseKey(key)
        
        progress_bar(4, total_steps, f"{status} Windows Update", "Completed!")
        
        return True
    except Exception as e:
        print_text(f"\nError: {e}", C.RED, 2)
        return False


def banner():
    width = shutil.get_terminal_size().columns

    print("")
    print((C.BOLD + C.BLUE + "╔══════════════════════════════════════════════╗" + C.RESET).center(width))
    print((C.BOLD + C.BLUE + "║       Windows Defender Controller            ║" + C.RESET).center(width))
    print((C.BOLD + C.BLUE + "║       Developed By : Rafid                   ║" + C.RESET).center(width))
    print((C.BOLD + C.BLUE + "╚══════════════════════════════════════════════╝" + C.RESET).center(width))
    print("")
    print("")

def main():
    # Check if running on Windows
    if os.name != "nt":
        print_text("This application only supports Windows operating system!", C.RED, 4)
        sys.exit(1)
        
    while True:
        clear_screen()
        banner()
        
        print_text("Select what you want to control:", C.CYAN, 2)
        print_text("1. Windows Defender", C.WHITE, 4)
        print_text("2. Windows Update", C.WHITE, 4)
        print_text("3. Exit", C.RED, 4)
        
        choice = input("\n  Enter your choice (1-3): ").strip()
        
        if choice == "1":
            # Windows Defender
            clear_screen()
            banner()
            print_text("Windows Defender Control", C.CYAN, 2)
            print_text("1. Enable Windows Defender", C.GREEN, 4)
            print_text("2. Disable Windows Defender", C.RED, 4)
            
            def_choice = input("\n  Enter your choice (1-2): ").strip()
            
            if def_choice == "1":
                result = def_con(True)
            elif def_choice == "2":
                result = def_con(False)
            else:
                print_text("Invalid choice!", C.RED, 2)
                input("\n  Press Enter to continue...")
                continue
                
        elif choice == "2":
            # Windows Update
            clear_screen()
            banner()
            print_text("Windows Update Control", C.CYAN, 2)
            print_text("1. Enable Windows Update", C.GREEN, 4)
            print_text("2. Disable Windows Update", C.RED, 4)
            
            up_choice = input("\n  Enter your choice (1-2): ").strip()
            
            if up_choice == "1":
                result = update_con(True)
            elif up_choice == "2":
                result = update_con(False)
            else:
                print_text("Invalid choice!", C.RED, 2)
                input("\n  Press Enter to continue...")
                continue
                
        elif choice == "3":
            clear_screen()
            print_text("Exiting... Goodbye!", C.GREEN, 2)
            break
            
        else:
            print_text("Invalid choice!", C.RED, 2)
            input("\n  Press Enter to continue...")
            continue
            
        input("\n  Press Enter to continue...")

if __name__ == "__main__":
    main()