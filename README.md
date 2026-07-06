# Def Con - Windows Defender & Update Controller

[![GitHub](https://img.shields.io/badge/GitHub-Repository-blue?style=flat-square&logo=github)](https://github.com/rafidahmed870/def-con)

A powerful and easy-to-use command-line tool to control Windows Defender and Windows Update settings on Windows operating systems.

## 📁 Repository

- **GitHub**: [https://github.com/rafidahmed870/def-con](https://github.com/rafidahmed870/def-con)

## Features

- 🛡️ **Windows Defender Control** - Enable or disable Windows Defender with a single command
- 🔄 **Windows Update Control** - Manage Windows Update settings easily
- 📊 **Beautiful Progress Bar** - Visual feedback for all operations
- 🎨 **Color-Coded UI** - Clean and intuitive terminal interface
- 💻 **Windows Only** - Optimized for Windows operating systems

## Requirements

- **Operating System**: Windows 10 or later
- **Python**: 3.8 or higher (for running from source)
- **Administrator Privileges**: Required to modify system registry settings

## Installation & Usage

### Option 1: Run from Source

1. **Clone the repository**:
   ```bash
   git clone https://github.com/rafidahmed870/def-con.git
   cd def-con
   ```
2. **Run as Administrator**:
   ```powershell
   python main.py
   ```
3. Follow the on-screen menu to control Windows Defender or Windows Update

### Option 2: Build EXE (Windows Only)

1. Double-click `build.bat`
2. The script will automatically:
   - Create a virtual environment
   - Install required dependencies
   - Build a standalone EXE
3. Find the built EXE in `dist\Def Con.exe`
4. Run the EXE **as Administrator**

## How to Use

1. **Launch the application** (as Administrator)
2. **Select an option** from the main menu:
   - `1` - Windows Defender Control
   - `2` - Windows Update Control
   - `3` - Exit
3. **Choose Enable or Disable** for the selected option
4. Wait for the operation to complete (watch the progress bar!)
5. Press Enter to continue or exit

## Screenshots

### Main Menu
```
╔══════════════════════════════════════════════╗
║       Windows Defender Controller            ║
║       Developed By : Rafid                   ║
╚══════════════════════════════════════════════╝


  Select what you want to control:
    1. Windows Defender
    2. Windows Update
    3. Exit

  Enter your choice (1-3):
```

### Progress Bar
```
Disabling Windows Defender |██████████████████████████████████████████████████| 100.0% Completed!
```

## Project Structure

```
def-con/
├── main.py              # Main application code
├── build.bat            # Build script for creating EXE
├── requirements.txt     # Python dependencies
├── rtlogo.ico           # Application icon
├── LICENSE              # MIT License
└── README.md            # This file
```

## Technologies Used

- **Python 3** - Core programming language
- **winreg** - Windows registry access
- **ctypes** - Windows API calls
- **PyInstaller** - For building standalone EXE

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

**Rafid Ahmed**

## Disclaimer

⚠️ **IMPORTANT**: Disabling Windows Defender and Windows Update can expose your system to security risks. This tool is intended for educational purposes and advanced users only. Use at your own risk. Always ensure you have alternative security measures in place when disabling Windows Defender.

## Support

If you encounter any issues or have questions, feel free to open an issue in the repository.
