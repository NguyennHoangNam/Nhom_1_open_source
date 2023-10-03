import tkinter as tk
from sympy import Symbol, Eq, solve

class AlgebraApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Algebra App")
        
        self.equation_label = tk.Label(root, text="Equation:")
        self.equation_label.pack()
        
        self.equation_entry = tk.Entry(root)
        self.equation_entry.pack()
        
        self.solve_button = tk.Button(root, text="Solve", command=self.solve_equation)
        self.solve_button.pack()
        
        self.result_label = tk.Label(root, text="")
        self.result_label.pack()
        
    def solve_equation(self):
        equation = self.equation_entry.get()
        x = Symbol('x')
        try:
            equation = Eq(eval(equation), 0)  # Convert the string equation to a SymPy equation
            solution = solve(equation, x)
            self.result_label.config(text="Solution: x = " + str(solution))
        except Exception as e:
            self.result_label.config(text="Error: " + str(e))

root = tk.Tk()
app = AlgebraApp(root)
root.mainloop()