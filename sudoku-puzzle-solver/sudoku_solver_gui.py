import tkinter as tk
from tkinter import messagebox
from solver import get_subgrid_size, solve_sudoku

class SudokuSolverGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")

        # Set window size and center it
        self.root.geometry("500x600")
        self.root.configure(bg="#f0f0f0")  # Light gray background

        # Create a title label
        self.title_label = tk.Label(root, text="Sudoku Solver", font=("Helvetica", 24), bg="#f0f0f0")
        self.title_label.pack(pady=10)

        # Update size options for grid sizes from 4x4 to 9x9
        self.size_options = {1: 4, 2: 5, 3: 6, 4: 7, 5: 9}
        self.size = 9  # Default grid size

        # Dropdown menu for selecting grid size
        self.size_label = tk.Label(root, text="Select Grid Size:", font=("Helvetica", 14), bg="#f0f0f0")
        self.size_label.pack(pady=5)

        self.size_var = tk.IntVar()
        self.size_var.set(5)  # Default to 5x5
        self.size_menu = tk.OptionMenu(root, self.size_var, *self.size_options.keys(), command=self.update_grid_size)
        self.size_menu.config(font=("Helvetica", 14))
        self.size_menu.pack(pady=5)

        # Create a frame for the grid input and center it
        self.grid_frame = tk.Frame(root, bg="#ffffff")
        self.grid_frame.pack(pady=10)

        # Buttons to start the solving process and reset the grid
        button_frame = tk.Frame(root, bg="#f0f0f0")
        button_frame.pack(pady=20)

        self.solve_button = tk.Button(button_frame, text="Solve", command=self.solve, bg="#4CAF50", fg="white", font=("Helvetica", 14), padx=10, pady=5)
        self.solve_button.pack(side=tk.LEFT, padx=10)

        self.reset_button = tk.Button(button_frame, text="Reset", command=self.reset_grid, bg="#f44336", fg="white", font=("Helvetica", 14), padx=10, pady=5)
        self.reset_button.pack(side=tk.LEFT)

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
                entry = tk.Entry(self.grid_frame, width=3, font=('Arial', 18), justify='center', bd=2, relief='solid')
                entry.grid(row=row, column=col, padx=2, pady=2)
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

    def reset_grid(self):
        # Clear all entries in the grid
        for row_entries in self.entries:
            for entry in row_entries:
                entry.delete(0, tk.END)

# Run the GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuSolverGUI(root)
    root.mainloop()
