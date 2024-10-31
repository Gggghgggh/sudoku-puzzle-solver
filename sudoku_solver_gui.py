import tkinter as tk
from tkinter import messagebox
from solver import get_subgrid_size, is_valid, solve_sudoku, find_empty

class SudokuSolverGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")

        self.size_options = {1: 4, 2: 5, 3: 6, 4: 7, 5: 9, 6: 12, 7: 16, 8: 25}
        self.size = 9  # Default grid size

        # Dropdown menu for selecting grid size
        self.size_label = tk.Label(root, text="Select Grid Size:")
        self.size_label.pack()
        self.size_var = tk.IntVar()
        self.size_var.set(5)  # Default to 9x9
        self.size_menu = tk.OptionMenu(root, self.size_var, *self.size_options.keys(), command=self.update_grid_size)
        self.size_menu.pack()

        # Create a frame for the grid input
        self.grid_frame = tk.Frame(root)
        self.grid_frame.pack()

        # Button to start the solving process
        self.solve_button = tk.Button(root, text="Solve", command=self.solve)
        self.solve_button.pack()

        # Initialize a 9x9 grid
        self.create_grid()

    def update_grid_size(self, choice):
        self.size = self.size_options.get(choice, 9)
        self.create_grid()

    def create_grid(self):
        # Clear previous grid if any
        for widget in self.grid_frame.winfo_children():
            widget.destroy()

        # Create entry widgets for grid input
        self.entries = []
        for row in range(self.size):
            row_entries = []
            for col in range(self.size):
                entry = tk.Entry(self.grid_frame, width=2, font=('Arial', 16), justify='center')
                entry.grid(row=row, column=col, padx=1, pady=1)
                row_entries.append(entry)
            self.entries.append(row_entries)

    def get_board(self):
        # Convert input entries into a 2D list of integers
        board = []
        for row_entries in self.entries:
            row = []
            for entry in row_entries:
                val = entry.get()
                row.append(int(val) if val.isdigit() else 0)
            board.append(row)
        return board

    def solve(self):
        board = self.get_board()
        if solve_sudoku(board, self.size):
            # Update the entries with the solution
            for i in range(self.size):
                for j in range(self.size):
                    self.entries[i][j].delete(0, tk.END)
                    self.entries[i][j].insert(0, str(board[i][j]))
            messagebox.showinfo("Success", "Sudoku solved successfully!")
        else:
            messagebox.showwarning("Failure", "No solution exists for the given puzzle.")

# Run the GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuSolverGUI(root)
    root.mainloop()
