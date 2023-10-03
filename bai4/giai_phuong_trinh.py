import tkinter as tk
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from sympy import sympify, symbols, lambdify

class FunctionPlotter:
    def __init__(self, root):
        self.root = root
        self.root.title("Function Plotter")
        
        self.canvas_width = 500
        self.canvas_height = 500
        
        self.canvas = tk.Canvas(root, width=self.canvas_width, height=self.canvas_height)
        self.canvas.pack()
        
        self.figure = Figure(figsize=(5, 5))
        self.ax = self.figure.add_subplot(111)
        
        self.canvas_widget = FigureCanvasTkAgg(self.figure, master=self.canvas)
        self.canvas_widget.get_tk_widget().pack()
        
        self.function_entry = tk.Entry(root)
        self.function_entry.pack()
        
        self.plot_button = tk.Button(root, text="Plot", command=self.plot_function)
        self.plot_button.pack()
        
        self.clear_button = tk.Button(root, text="Clear", command=self.clear_plot)
        self.clear_button.pack()
        
    def plot_function(self):
        function_str = self.function_entry.get()
        x = symbols('x')
        
        try:
            function = sympify(function_str)
            func_lambda = lambdify(x, function, "numpy")
            
            x_vals = np.linspace(-10, 10, 400)
            y_vals = func_lambda(x_vals)
            
            self.ax.plot(x_vals, y_vals)
            self.ax.axhline(0, color='black', linewidth=0.5)
            self.ax.axvline(0, color='black', linewidth=0.5)
            self.canvas_widget.draw()
        except Exception as e:
            print("Error:", e)
    
    def clear_plot(self):
        self.ax.clear()
        self.canvas_widget.draw()
    
root = tk.Tk()
app = FunctionPlotter(root)
root.mainloop()