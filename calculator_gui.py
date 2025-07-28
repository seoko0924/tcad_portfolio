#!/usr/bin/env python3
"""
GUI Calculator
A graphical calculator with basic and scientific functions using tkinter.
"""

import tkinter as tk
from tkinter import ttk, messagebox
import math


class CalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Calculator")
        self.root.geometry("400x600")
        self.root.resizable(False, False)
        
        # Variables
        self.display_var = tk.StringVar()
        self.display_var.set("0")
        self.memory = 0
        self.history = []
        self.current_input = ""
        self.operator = ""
        self.previous_value = 0
        self.waiting_for_number = False
        
        self.setup_ui()
    
    def setup_ui(self):
        """Setup the user interface"""
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Display
        display_frame = ttk.Frame(main_frame)
        display_frame.grid(row=0, column=0, columnspan=4, sticky=(tk.W, tk.E), pady=(0, 10))
        
        self.display = ttk.Entry(
            display_frame, 
            textvariable=self.display_var, 
            state="readonly",
            font=("Arial", 16),
            justify="right"
        )
        self.display.grid(row=0, column=0, sticky=(tk.W, tk.E))
        display_frame.columnconfigure(0, weight=1)
        
        # Memory indicator
        self.memory_label = ttk.Label(main_frame, text="", font=("Arial", 8))
        self.memory_label.grid(row=1, column=0, columnspan=4, sticky=(tk.W,))
        
        # Button style configuration
        style = ttk.Style()
        style.configure("Number.TButton", width=8, padding=5)
        style.configure("Operator.TButton", width=8, padding=5)
        style.configure("Function.TButton", width=8, padding=5)
        
        # Create buttons
        self.create_buttons(main_frame)
        
        # Configure grid weights
        for i in range(4):
            main_frame.columnconfigure(i, weight=1)
    
    def create_buttons(self, parent):
        """Create calculator buttons"""
        # Row 2: Memory and Clear functions
        ttk.Button(parent, text="MC", command=self.memory_clear, style="Function.TButton").grid(row=2, column=0, padx=2, pady=2)
        ttk.Button(parent, text="MR", command=self.memory_recall, style="Function.TButton").grid(row=2, column=1, padx=2, pady=2)
        ttk.Button(parent, text="MS", command=self.memory_store, style="Function.TButton").grid(row=2, column=2, padx=2, pady=2)
        ttk.Button(parent, text="C", command=self.clear, style="Function.TButton").grid(row=2, column=3, padx=2, pady=2)
        
        # Row 3: Scientific functions
        ttk.Button(parent, text="sin", command=lambda: self.scientific_function("sin"), style="Function.TButton").grid(row=3, column=0, padx=2, pady=2)
        ttk.Button(parent, text="cos", command=lambda: self.scientific_function("cos"), style="Function.TButton").grid(row=3, column=1, padx=2, pady=2)
        ttk.Button(parent, text="tan", command=lambda: self.scientific_function("tan"), style="Function.TButton").grid(row=3, column=2, padx=2, pady=2)
        ttk.Button(parent, text="log", command=lambda: self.scientific_function("log"), style="Function.TButton").grid(row=3, column=3, padx=2, pady=2)
        
        # Row 4: More scientific functions
        ttk.Button(parent, text="ln", command=lambda: self.scientific_function("ln"), style="Function.TButton").grid(row=4, column=0, padx=2, pady=2)
        ttk.Button(parent, text="√", command=lambda: self.scientific_function("sqrt"), style="Function.TButton").grid(row=4, column=1, padx=2, pady=2)
        ttk.Button(parent, text="x²", command=lambda: self.scientific_function("square"), style="Function.TButton").grid(row=4, column=2, padx=2, pady=2)
        ttk.Button(parent, text="x^y", command=lambda: self.operator_click("^"), style="Operator.TButton").grid(row=4, column=3, padx=2, pady=2)
        
        # Row 5: Numbers and operators
        ttk.Button(parent, text="7", command=lambda: self.number_click("7"), style="Number.TButton").grid(row=5, column=0, padx=2, pady=2)
        ttk.Button(parent, text="8", command=lambda: self.number_click("8"), style="Number.TButton").grid(row=5, column=1, padx=2, pady=2)
        ttk.Button(parent, text="9", command=lambda: self.number_click("9"), style="Number.TButton").grid(row=5, column=2, padx=2, pady=2)
        ttk.Button(parent, text="÷", command=lambda: self.operator_click("/"), style="Operator.TButton").grid(row=5, column=3, padx=2, pady=2)
        
        # Row 6
        ttk.Button(parent, text="4", command=lambda: self.number_click("4"), style="Number.TButton").grid(row=6, column=0, padx=2, pady=2)
        ttk.Button(parent, text="5", command=lambda: self.number_click("5"), style="Number.TButton").grid(row=6, column=1, padx=2, pady=2)
        ttk.Button(parent, text="6", command=lambda: self.number_click("6"), style="Number.TButton").grid(row=6, column=2, padx=2, pady=2)
        ttk.Button(parent, text="×", command=lambda: self.operator_click("*"), style="Operator.TButton").grid(row=6, column=3, padx=2, pady=2)
        
        # Row 7
        ttk.Button(parent, text="1", command=lambda: self.number_click("1"), style="Number.TButton").grid(row=7, column=0, padx=2, pady=2)
        ttk.Button(parent, text="2", command=lambda: self.number_click("2"), style="Number.TButton").grid(row=7, column=1, padx=2, pady=2)
        ttk.Button(parent, text="3", command=lambda: self.number_click("3"), style="Number.TButton").grid(row=7, column=2, padx=2, pady=2)
        ttk.Button(parent, text="−", command=lambda: self.operator_click("-"), style="Operator.TButton").grid(row=7, column=3, padx=2, pady=2)
        
        # Row 8
        ttk.Button(parent, text="0", command=lambda: self.number_click("0"), style="Number.TButton").grid(row=8, column=0, padx=2, pady=2)
        ttk.Button(parent, text=".", command=lambda: self.number_click("."), style="Number.TButton").grid(row=8, column=1, padx=2, pady=2)
        ttk.Button(parent, text="±", command=self.toggle_sign, style="Function.TButton").grid(row=8, column=2, padx=2, pady=2)
        ttk.Button(parent, text="+", command=lambda: self.operator_click("+"), style="Operator.TButton").grid(row=8, column=3, padx=2, pady=2)
        
        # Row 9: Equals and additional functions
        ttk.Button(parent, text="=", command=self.equals_click, style="Operator.TButton").grid(row=9, column=0, columnspan=2, padx=2, pady=2, sticky=(tk.W, tk.E))
        ttk.Button(parent, text="π", command=lambda: self.constant_click(math.pi), style="Function.TButton").grid(row=9, column=2, padx=2, pady=2)
        ttk.Button(parent, text="e", command=lambda: self.constant_click(math.e), style="Function.TButton").grid(row=9, column=3, padx=2, pady=2)
        
        # Row 10: History button
        ttk.Button(parent, text="History", command=self.show_history, style="Function.TButton").grid(row=10, column=0, columnspan=4, padx=2, pady=2, sticky=(tk.W, tk.E))
    
    def number_click(self, number):
        """Handle number button clicks"""
        if self.waiting_for_number:
            self.display_var.set(number)
            self.waiting_for_number = False
        else:
            current = self.display_var.get()
            if current == "0" and number != ".":
                self.display_var.set(number)
            else:
                self.display_var.set(current + number)
    
    def operator_click(self, op):
        """Handle operator button clicks"""
        try:
            current_value = float(self.display_var.get())
            
            if self.operator and not self.waiting_for_number:
                self.calculate()
                current_value = float(self.display_var.get())
            
            self.previous_value = current_value
            self.operator = op
            self.waiting_for_number = True
            
        except ValueError:
            messagebox.showerror("Error", "Invalid input")
    
    def equals_click(self):
        """Handle equals button click"""
        self.calculate()
    
    def calculate(self):
        """Perform calculation"""
        try:
            current_value = float(self.display_var.get())
            
            if self.operator == "+":
                result = self.previous_value + current_value
            elif self.operator == "-":
                result = self.previous_value - current_value
            elif self.operator == "*":
                result = self.previous_value * current_value
            elif self.operator == "/":
                if current_value == 0:
                    raise ValueError("Cannot divide by zero")
                result = self.previous_value / current_value
            elif self.operator == "^":
                result = self.previous_value ** current_value
            else:
                return
            
            # Add to history
            operation = f"{self.previous_value} {self.operator} {current_value} = {result}"
            self.history.append(operation)
            
            self.display_var.set(str(result))
            self.operator = ""
            self.waiting_for_number = True
            
        except (ValueError, ZeroDivisionError) as e:
            messagebox.showerror("Error", str(e))
            self.clear()
    
    def scientific_function(self, func):
        """Handle scientific function buttons"""
        try:
            value = float(self.display_var.get())
            
            if func == "sin":
                result = math.sin(math.radians(value))
            elif func == "cos":
                result = math.cos(math.radians(value))
            elif func == "tan":
                result = math.tan(math.radians(value))
            elif func == "log":
                if value <= 0:
                    raise ValueError("Logarithm undefined for non-positive numbers")
                result = math.log10(value)
            elif func == "ln":
                if value <= 0:
                    raise ValueError("Natural log undefined for non-positive numbers")
                result = math.log(value)
            elif func == "sqrt":
                if value < 0:
                    raise ValueError("Square root undefined for negative numbers")
                result = math.sqrt(value)
            elif func == "square":
                result = value ** 2
            else:
                return
            
            # Add to history
            operation = f"{func}({value}) = {result}"
            self.history.append(operation)
            
            self.display_var.set(str(result))
            self.waiting_for_number = True
            
        except (ValueError, OverflowError) as e:
            messagebox.showerror("Error", str(e))
    
    def constant_click(self, value):
        """Handle constant button clicks (π, e)"""
        self.display_var.set(str(value))
        self.waiting_for_number = True
    
    def toggle_sign(self):
        """Toggle the sign of the current number"""
        try:
            current = float(self.display_var.get())
            self.display_var.set(str(-current))
        except ValueError:
            pass
    
    def clear(self):
        """Clear the calculator"""
        self.display_var.set("0")
        self.operator = ""
        self.previous_value = 0
        self.waiting_for_number = False
    
    def memory_store(self):
        """Store current value in memory"""
        try:
            self.memory = float(self.display_var.get())
            self.memory_label.config(text="M")
        except ValueError:
            pass
    
    def memory_recall(self):
        """Recall value from memory"""
        self.display_var.set(str(self.memory))
        self.waiting_for_number = True
    
    def memory_clear(self):
        """Clear memory"""
        self.memory = 0
        self.memory_label.config(text="")
    
    def show_history(self):
        """Show calculation history in a popup window"""
        history_window = tk.Toplevel(self.root)
        history_window.title("Calculation History")
        history_window.geometry("400x300")
        
        # History text widget with scrollbar
        frame = ttk.Frame(history_window)
        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        scrollbar = ttk.Scrollbar(frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        history_text = tk.Text(frame, yscrollcommand=scrollbar.set, state=tk.DISABLED)
        history_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        scrollbar.config(command=history_text.yview)
        
        # Populate history
        history_text.config(state=tk.NORMAL)
        if self.history:
            for calculation in self.history[-20:]:  # Show last 20 calculations
                history_text.insert(tk.END, calculation + "\n")
        else:
            history_text.insert(tk.END, "No calculations in history")
        history_text.config(state=tk.DISABLED)
        
        # Clear history button
        ttk.Button(
            history_window, 
            text="Clear History", 
            command=lambda: self.clear_history(history_text)
        ).pack(pady=5)
    
    def clear_history(self, text_widget):
        """Clear calculation history"""
        self.history.clear()
        text_widget.config(state=tk.NORMAL)
        text_widget.delete(1.0, tk.END)
        text_widget.insert(tk.END, "History cleared")
        text_widget.config(state=tk.DISABLED)


def main():
    """Main function to run the GUI calculator"""
    root = tk.Tk()
    app = CalculatorGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()