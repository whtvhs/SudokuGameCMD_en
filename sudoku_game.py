import random
import sys
import os


class SudokuGame:
    def __init__(self, theme='light'):
        self.size = 9
        self.cursor = [0, 0]
        self.theme = theme
        self.command_history = []
        self.max_history = 5
        self.generate_sudoku()

    def clear_screen(self):
        """Clears the terminal screen"""
        os.system('cls' if os.name == 'nt' else 'clear')

    def get_theme_colors(self):
        """Returns color codes for current theme"""
        if self.theme == 'dark':
            return {
                'text': '\033[37m',  # white
                'border': '\033[36m',  # cyan
                'cursor': '\033[41m',  # red background
                'fixed': '\033[33m',  # yellow
                'input': '\033[32m',  # green
                'error': '\033[31m',  # red
                'success': '\033[32m',  # green
                'reset': '\033[0m',
                'title': '\033[1;36m',  # bold cyan
                'highlight': '\033[1;35m'  # bold magenta
            }
        else:  # light theme
            return {
                'text': '\033[30m',  # black
                'border': '\033[34m',  # blue
                'cursor': '\033[44m',  # blue background
                'fixed': '\033[33m',  # yellow
                'input': '\033[32m',  # green
                'error': '\033[31m',  # red
                'success': '\033[32m',  # green
                'reset': '\033[0m',
                'title': '\033[1;34m',  # bold blue
                'highlight': '\033[1;35m'  # bold magenta
            }

    def generate_sudoku(self):
        """Generates a new Sudoku puzzle"""
        # Base solution
        base = [
            [5, 3, 4, 6, 7, 8, 9, 1, 2],
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 9]
        ]

        # Shuffle rows and columns
        for _ in range(10):
            # Swap rows within 3x3 blocks
            block = random.randint(0, 2) * 3
            r1 = block + random.randint(0, 2)
            r2 = block + random.randint(0, 2)
            base[r1], base[r2] = base[r2], base[r1]

            # Swap columns within 3x3 blocks
            block = random.randint(0, 2) * 3
            c1 = block + random.randint(0, 2)
            c2 = block + random.randint(0, 2)
            for row in base:
                row[c1], row[c2] = row[c2], row[c1]

        # Create copies for the game
        self.solution = [row[:] for row in base]
        self.initial_board = [row[:] for row in base]
        self.board = [row[:] for row in base]

        # Remove numbers to create puzzle
        cells = [(r, c) for r in range(9) for c in range(9)]
        random.shuffle(cells)

        to_remove = random.randint(40, 50)
        for i in range(to_remove):
            r, c = cells[i]
            self.initial_board[r][c] = 0
            self.board[r][c] = 0

    def display_game_window(self):
        """Displays the game window"""
        colors = self.get_theme_colors()

        # Clear screen
        self.clear_screen()

        # Window header
        print(f"{colors['title']}{'=' * 60}{colors['reset']}")
        print(f"{colors['title']}               SUDOKU COMMAND GAME               {colors['reset']}")
        print(f"{colors['title']}{'=' * 60}{colors['reset']}")
        print(f"Theme: {colors['highlight']}{'Dark' if self.theme == 'dark' else 'Light'}{colors['reset']} | "
              f"Cursor: row {colors['highlight']}{self.cursor[0] + 1}{colors['reset']}, "
              f"column {colors['highlight']}{self.cursor[1] + 1}{colors['reset']}")
        print(f"{colors['border']}{'-' * 60}{colors['reset']}")

        # Sudoku grid
        print()
        print(f"{colors['text']}   1 2 3   4 5 6   7 8 9{colors['reset']}")
        print(f"{colors['border']}  {'-' * 25}{colors['reset']}")

        for i in range(9):
            # Row number
            row_num = i + 1
            row_display = f"{colors['text']}{row_num} {colors['reset']}{colors['border']}|{colors['reset']}"

            for j in range(9):
                # Display cell
                if self.cursor == [i, j]:
                    # Cell with cursor
                    if self.board[i][j] == 0:
                        cell = f"{colors['cursor']}  {colors['reset']}"
                    else:
                        cell = f"{colors['cursor']}{self.board[i][j]:^2}{colors['reset']}"
                else:
                    # Normal cell
                    if self.board[i][j] == 0:
                        cell = f"{colors['text']} .{colors['reset']}"
                    else:
                        if self.initial_board[i][j] != 0:
                            # Original numbers
                            cell = f"{colors['fixed']}{self.board[i][j]:^2}{colors['reset']}"
                        else:
                            # Player numbers
                            cell = f"{colors['input']}{self.board[i][j]:^2}{colors['reset']}"

                row_display += f" {cell}"

                # Add block separators
                if j == 2 or j == 5:
                    row_display += f" {colors['border']}|{colors['reset']}"
                elif j == 8:
                    row_display += f" {colors['border']}|{colors['reset']}"

            print(row_display)

            # Horizontal block separators
            if i == 2 or i == 5:
                print(f"{colors['border']}  {'-' * 25}{colors['reset']}")

        print(f"{colors['border']}  {'-' * 25}{colors['reset']}")

        # Separator between board and command line
        print(f"\n{colors['border']}{'=' * 60}{colors['reset']}")

        # Command line section
        print(f"\n{colors['title']}COMMAND LINE:{colors['reset']}")
        print(f"{colors['border']}{'-' * 60}{colors['reset']}")

        # Command history
        if self.command_history:
            print(f"{colors['text']}Recent commands:{colors['reset']}")
            for cmd in self.command_history[-self.max_history:]:
                print(f"  {colors['input']}>{colors['reset']} {cmd}")
            print()

        # Available commands in two columns
        print(f"{colors['text']}Available commands:{colors['reset']}")
        commands_left = [
            f"{colors['input']}left(n){colors['reset']} - move left n cells",
            f"{colors['input']}right(n){colors['reset']} - move right n cells",
            f"{colors['input']}up(n){colors['reset']} - move up n cells",
            f"{colors['input']}down(n){colors['reset']} - move down n cells",
            f"{colors['input']}1-9{colors['reset']} - insert number"
        ]

        commands_right = [
            f"{colors['input']}0{colors['reset']} - clear cell",
            f"{colors['input']}space{colors['reset']} - clear cell",
            f"{colors['input']}restart{colors['reset']} - new game",
            f"{colors['input']}theme{colors['reset']} - switch theme",
            f"{colors['input']}help{colors['reset']} - show help",
            f"{colors['input']}quit{colors['reset']} - exit game"
        ]

        # Print commands in two columns
        for i in range(max(len(commands_left), len(commands_right))):
            left = commands_left[i] if i < len(commands_left) else ""
            right = commands_right[i] if i < len(commands_right) else ""
            print(f"  {left:<30}  {right}")

        print(f"{colors['border']}{'-' * 60}{colors['reset']}")

    def add_to_history(self, message):
        """Adds message to command history"""
        self.command_history.append(message)
        if len(self.command_history) > self.max_history:
            self.command_history.pop(0)

    def move_cursor(self, direction, steps=1):
        """Moves the cursor"""
        steps = max(1, min(steps, 8))

        old_pos = self.cursor.copy()

        if direction == "left":
            self.cursor[1] = max(0, self.cursor[1] - steps)
        elif direction == "right":
            self.cursor[1] = min(8, self.cursor[1] + steps)
        elif direction == "up":
            self.cursor[0] = max(0, self.cursor[0] - steps)
        elif direction == "down":
            self.cursor[0] = min(8, self.cursor[0] + steps)

        # Add to history only if position changed
        if old_pos != self.cursor:
            self.add_to_history(f"{direction}({steps})")

    def insert_number(self, num):
        """Inserts a number at current cursor position"""
        row, col = self.cursor

        # Check if cell can be modified
        if self.initial_board[row][col] != 0:
            self.add_to_history(f"Error: cell [{row + 1},{col + 1}] is fixed")
            return False

        if num == 0:
            self.board[row][col] = 0
            self.add_to_history(f"Cell [{row + 1},{col + 1}] cleared")
        else:
            # Check if number can be placed
            if self.is_valid_move(row, col, num):
                self.board[row][col] = num
                self.add_to_history(f"Number {num} placed at [{row + 1},{col + 1}]")

                if self.check_win():
                    return True
            else:
                self.add_to_history(f"Error: cannot place {num} at [{row + 1},{col + 1}]")

        return False

    def is_valid_move(self, row, col, num):
        """Checks if a number can be placed in a cell"""
        # Check row
        for j in range(9):
            if self.board[row][j] == num and j != col:
                return False

        # Check column
        for i in range(9):
            if self.board[i][col] == num and i != row:
                return False

        # Check 3x3 box
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if self.board[i][j] == num and (i != row or j != col):
                    return False

        return True

    def check_win(self):
        """Checks if Sudoku is solved"""
        # Check for empty cells
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    return False

        # Check rows
        for i in range(9):
            row = self.board[i]
            if sorted(row) != list(range(1, 10)):
                return False

        # Check columns
        for j in range(9):
            col = [self.board[i][j] for i in range(9)]
            if sorted(col) != list(range(1, 10)):
                return False

        # Check 3x3 boxes
        for box_i in range(0, 9, 3):
            for box_j in range(0, 9, 3):
                square = []
                for i in range(3):
                    for j in range(3):
                        square.append(self.board[box_i + i][box_j + j])
                if sorted(square) != list(range(1, 10)):
                    return False

        return True

    def show_help(self):
        """Shows help information"""
        colors = self.get_theme_colors()

        self.clear_screen()
        print(f"{colors['title']}{'=' * 60}{colors['reset']}")
        print(f"{colors['title']}                      HELP                        {colors['reset']}")
        print(f"{colors['title']}{'=' * 60}{colors['reset']}")
        print()
        print(f"{colors['text']}Game Objective:{colors['reset']}")
        print("  Fill all cells with numbers 1-9 so that each")
        print("  number appears only once in each row, column,")
        print("  and 3x3 box.")
        print()
        print(f"{colors['text']}Controls:{colors['reset']}")
        print(f"  {colors['input']}left(n){colors['reset']}  - move cursor left n cells")
        print(f"  {colors['input']}right(n){colors['reset']} - move cursor right n cells")
        print(f"  {colors['input']}up(n){colors['reset']}    - move cursor up n cells")
        print(f"  {colors['input']}down(n){colors['reset']}  - move cursor down n cells")
        print(f"  {colors['input']}1-9{colors['reset']}     - insert corresponding number")
        print(f"  {colors['input']}0{colors['reset']}       - clear current cell")
        print(f"  {colors['input']}space{colors['reset']}   - also clear current cell")
        print()
        print(f"{colors['text']}Other commands:{colors['reset']}")
        print(f"  {colors['input']}restart{colors['reset']} - start new game")
        print(f"  {colors['input']}theme{colors['reset']}   - switch theme (light/dark)")
        print(f"  {colors['input']}help{colors['reset']}    - show this help")
        print(f"  {colors['input']}quit{colors['reset']}    - exit game")
        print()
        print(f"{colors['text']}Symbols:{colors['reset']}")
        print(f"  {colors['fixed']} 5 {colors['reset']} - original number (cannot change)")
        print(f"  {colors['input']} 3 {colors['reset']} - number entered by player")
        print(f"  {colors['cursor']}[7]{colors['reset']} - current cursor position")
        print(f"  {colors['text']} .{colors['reset']}  - empty cell")
        print()
        print(f"{colors['border']}{'-' * 60}{colors['reset']}")
        input(f"\n{colors['input']}Press Enter to return to game...{colors['reset']}")

    def switch_theme(self):
        """Switches between light and dark themes"""
        self.theme = 'dark' if self.theme == 'light' else 'light'
        self.add_to_history(f"Theme switched to {'dark' if self.theme == 'dark' else 'light'}")

    def restart_game(self):
        """Restarts the game with new puzzle"""
        self.cursor = [0, 0]
        self.generate_sudoku()
        self.command_history = []
        self.add_to_history("New game started")

    def parse_command(self, command):
        """Parses and executes a command"""
        cmd = command.strip().lower()

        if cmd in ["quit", "exit", "close"]:
            print("Thank you for playing!")
            sys.exit(0)

        elif cmd == "restart":
            self.restart_game()
            return False

        elif cmd == "theme":
            self.switch_theme()
            return False

        elif cmd == "help":
            self.show_help()
            return False

        elif cmd == "":
            return False

        # Movement commands
        elif cmd.startswith("left"):
            steps = 1
            if "(" in cmd and ")" in cmd:
                try:
                    steps_str = cmd.split("(")[1].split(")")[0]
                    if steps_str:
                        steps = int(steps_str)
                except:
                    steps = 1
            self.move_cursor("left", steps)
            return False

        elif cmd.startswith("right"):
            steps = 1
            if "(" in cmd and ")" in cmd:
                try:
                    steps_str = cmd.split("(")[1].split(")")[0]
                    if steps_str:
                        steps = int(steps_str)
                except:
                    steps = 1
            self.move_cursor("right", steps)
            return False

        elif cmd.startswith("up"):
            steps = 1
            if "(" in cmd and ")" in cmd:
                try:
                    steps_str = cmd.split("(")[1].split(")")[0]
                    if steps_str:
                        steps = int(steps_str)
                except:
                    steps = 1
            self.move_cursor("up", steps)
            return False

        elif cmd.startswith("down"):
            steps = 1
            if "(" in cmd and ")" in cmd:
                try:
                    steps_str = cmd.split("(")[1].split(")")[0]
                    if steps_str:
                        steps = int(steps_str)
                except:
                    steps = 1
            self.move_cursor("down", steps)
            return False

        # Number input
        elif cmd == " " or cmd == "space":
            return self.insert_number(0)

        elif cmd.isdigit() and 0 <= int(cmd) <= 9:
            return self.insert_number(int(cmd))

        else:
            self.add_to_history(f"Unknown command: {cmd}")
            return False

    def run(self):
        """Starts the game loop"""
        while True:
            try:
                # Display game window
                self.display_game_window()

                # Get command
                colors = self.get_theme_colors()
                command = input(f"\n{colors['input']}Enter command > {colors['reset']}")

                # Process command
                win = self.parse_command(command)

                # If game is won
                if win:
                    self.display_game_window()
                    colors = self.get_theme_colors()
                    print(f"\n{colors['success']}{'★' * 30}{colors['reset']}")
                    print(f"{colors['success']}        CONGRATULATIONS! SUDOKU SOLVED!       {colors['reset']}")
                    print(f"{colors['success']}{'★' * 30}{colors['reset']}")

                    choice = input(f"\n{colors['input']}New game? (yes/no): {colors['reset']}").lower()
                    if choice in ["yes", "y", "да", "д"]:
                        self.restart_game()
                    else:
                        print("Thank you for playing!")
                        sys.exit(0)

            except KeyboardInterrupt:
                print("\n\nGame interrupted.")
                sys.exit(0)
            except Exception as e:
                print(f"\nError: {e}")
                input("Press Enter to continue...")


def main():
    """Main entry point"""
    # Clear screen on startup
    os.system('cls' if os.name == 'nt' else 'clear')

    print("=" * 60)
    print("              SUDOKU COMMAND GAME")
    print("=" * 60)
    print()
    print("Choose theme:")
    print("  1. Light (default)")
    print("  2. Dark")
    print()

    while True:
        choice = input("Your choice (1/2): ").strip()
        if choice in ["1", "2", ""]:
            theme = 'dark' if choice == '2' else 'light'
            break
        else:
            print("Please enter 1 or 2")

    # Start the game
    game = SudokuGame(theme)
    game.run()


if __name__ == "__main__":
    main()