# SudokuGameCMD_en
# SudokuGameCMD_en
# 🎮 Sudoku with Command Control

**A terminal-based Sudoku game with unique command-based control system and theme support.**

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows%20|%20Linux%20|%20macOS-lightgrey.svg)]()

## 📋 Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Gameplay](#gameplay)
- [Commands](#commands)
- [Themes](#themes)
- [Project Structure](#project-structure)
- [Development](#development)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features

- **🎯 Unique Command Control** - Move cursor with commands like `left(2)`, `right(3)`
- **🎨 Dual Themes** - Light and dark themes with color coding
- **🔢 Intelligent Generation** - Always solvable puzzles with varying difficulty
- **📊 Visual Display** - Clear grid with cursor highlighting and number types
- **📝 Command History** - Track recent actions
- **✅ Input Validation** - Real-time Sudoku rule checking
- **🔄 Game Restart** - Instant new puzzle generation

## 🚀 Installation

### Requirements
- Python 3.7 or higher
- Terminal with ANSI color support

### Installation from Source

1. Clone the repository:
```bash
git clone https://github.com/your-username/sudoku-command-game.git
cd sudoku-command-game
```

2. (Optional) Create virtual environment:
```bash
python -m venv venv
# For Windows:
venv\Scripts\activate
# For Linux/Mac:
source venv/bin/activate
```

3. Run the game:
```bash
python sudoku_game.py
```

## 🎮 Gameplay

### Game Objective
Fill all cells with numbers 1-9 so that:
- Each number appears only once in each row
- Each number appears only once in each column
- Each number appears only once in each 3×3 box

### Starting the Game
When you launch the game, you'll see:
1. Theme selection
2. Game board with cursor at position [1,1]
3. Command line with hints

## ⌨️ Commands

### Cursor Movement
```
left(n)     - move cursor left n cells
right(n)    - move cursor right n cells
up(n)       - move cursor up n cells
down(n)     - move cursor down n cells
```
*Example: `left(2)` - move 2 cells left*

### Number Input
```
1-9         - insert corresponding digit
0           - clear current cell
space       - also clear current cell
```

### System Commands
```
restart     - start new game
theme       - switch theme (light/dark)
help        - show command help
quit        - exit game
exit        - exit game
close       - exit game
```

## 🎨 Themes

### Light Theme
- White background with black text
- Blue borders and cursor
- Yellow original numbers
- Green player numbers

### Dark Theme
- Black background with white text
- Cyan borders
- Red cursor
- Yellow original numbers
- Green player numbers

### Board Symbols
```
 5  - yellow: original number (cannot change)
 3  - green: number entered by player
[7] - red/blue: current cursor position
 .  - empty cell
```

## 📁 Project Structure

```
sudoku-command-game/
├── sudoku_game.py          # Main game file
├── README.md              # This file
├── requirements.txt       # Dependencies (if any)
└── LICENSE               # MIT License
```

### Game Classes
- **`SudokuGame`** - main game class
  - Sudoku generation and solving
  - Cursor control and input handling
  - Interface rendering
  - Command processing

## 💻 Development

### Architecture
The game follows object-oriented programming principles:
- **Model** - Sudoku generation and validation
- **View** - Interface rendering with color coding
- **Controller** - User command processing

### Algorithms
- **Sudoku generation**: Create complete solution then remove numbers
- **Validity checking**: Verify rows, columns, and 3×3 boxes
- **Solution search**: Backtracking algorithm

### Possible Improvements
- [ ] Save and load progress
- [ ] Difficulty levels
- [ ] Hints and auto-solve
- [ ] Error highlighting
- [ ] Timer and statistics
- [ ] Graphical interface (Tkinter/PyGame)

## 🧪 Testing

To verify functionality:
1. Ensure all commands work correctly
2. Test generation of different puzzles
3. Verify win condition checking
4. Test in different terminals

## 🤝 Contributing

Contributions are welcome! Here's how:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

⭐ **If you like this project, please give it a star!** ⭐

---

## 🎯 Game Tips

1. Start by looking for obvious numbers
2. Use movement commands for quick navigation
3. Switch themes for comfortable play at different times
4. Don't hesitate to use `restart` if stuck
5. Memorize common commands for more efficient play

**Good luck solving Sudoku!** 🧩

