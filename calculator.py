#!/usr/bin/env python3
"""
Advanced Calculator
A comprehensive calculator with basic arithmetic and scientific functions.
Useful for TCAD simulations and general calculations.
"""

import math
import sys


class Calculator:
    """A comprehensive calculator class with basic and scientific operations."""
    
    def __init__(self):
        self.history = []
        self.memory = 0
    
    def add(self, a, b):
        """Addition"""
        return a + b
    
    def subtract(self, a, b):
        """Subtraction"""
        return a - b
    
    def multiply(self, a, b):
        """Multiplication"""
        return a * b
    
    def divide(self, a, b):
        """Division with zero-check"""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    
    def power(self, base, exponent):
        """Exponentiation"""
        return base ** exponent
    
    def square_root(self, x):
        """Square root"""
        if x < 0:
            raise ValueError("Cannot take square root of negative number")
        return math.sqrt(x)
    
    def logarithm(self, x, base=10):
        """Logarithm (default base 10)"""
        if x <= 0:
            raise ValueError("Logarithm undefined for non-positive numbers")
        if base == 10:
            return math.log10(x)
        elif base == math.e:
            return math.log(x)
        else:
            return math.log(x) / math.log(base)
    
    def natural_log(self, x):
        """Natural logarithm"""
        return self.logarithm(x, math.e)
    
    def sin(self, x, degrees=False):
        """Sine function"""
        if degrees:
            x = math.radians(x)
        return math.sin(x)
    
    def cos(self, x, degrees=False):
        """Cosine function"""
        if degrees:
            x = math.radians(x)
        return math.cos(x)
    
    def tan(self, x, degrees=False):
        """Tangent function"""
        if degrees:
            x = math.radians(x)
        return math.tan(x)
    
    def factorial(self, n):
        """Factorial function"""
        if n < 0:
            raise ValueError("Factorial undefined for negative numbers")
        if not isinstance(n, int):
            raise ValueError("Factorial only defined for integers")
        return math.factorial(n)
    
    def percentage(self, value, percent):
        """Calculate percentage of a value"""
        return (value * percent) / 100
    
    def memory_store(self, value):
        """Store value in memory"""
        self.memory = value
        return f"Stored {value} in memory"
    
    def memory_recall(self):
        """Recall value from memory"""
        return self.memory
    
    def memory_clear(self):
        """Clear memory"""
        self.memory = 0
        return "Memory cleared"
    
    def add_to_history(self, operation, result):
        """Add calculation to history"""
        self.history.append(f"{operation} = {result}")
    
    def show_history(self):
        """Display calculation history"""
        if not self.history:
            return "No calculations in history"
        return "\n".join(self.history[-10:])  # Show last 10 calculations
    
    def clear_history(self):
        """Clear calculation history"""
        self.history.clear()
        return "History cleared"


def print_menu():
    """Print the calculator menu"""
    print("\n" + "="*50)
    print("           ADVANCED CALCULATOR")
    print("="*50)
    print("Basic Operations:")
    print("  1. Addition (+)")
    print("  2. Subtraction (-)")
    print("  3. Multiplication (*)")
    print("  4. Division (/)")
    print("  5. Power (^)")
    print("  6. Square Root (√)")
    print("\nScientific Functions:")
    print("  7. Logarithm (log)")
    print("  8. Natural Log (ln)")
    print("  9. Sine (sin)")
    print(" 10. Cosine (cos)")
    print(" 11. Tangent (tan)")
    print(" 12. Factorial (!)")
    print(" 13. Percentage (%)")
    print("\nMemory Functions:")
    print(" 14. Memory Store (MS)")
    print(" 15. Memory Recall (MR)")
    print(" 16. Memory Clear (MC)")
    print("\nUtility:")
    print(" 17. Show History")
    print(" 18. Clear History")
    print(" 19. Expression Calculator")
    print("  0. Exit")
    print("="*50)


def get_number(prompt):
    """Get a number from user input with error handling"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def evaluate_expression(expression, calc):
    """Safely evaluate mathematical expressions"""
    try:
        # Replace common mathematical functions
        expression = expression.replace('^', '**')
        expression = expression.replace('π', str(math.pi))
        expression = expression.replace('e', str(math.e))
        
        # Define safe functions for evaluation
        safe_dict = {
            "__builtins__": {},
            "abs": abs,
            "round": round,
            "min": min,
            "max": max,
            "sum": sum,
            "pow": pow,
            "sqrt": math.sqrt,
            "sin": math.sin,
            "cos": math.cos,
            "tan": math.tan,
            "log": math.log,
            "log10": math.log10,
            "exp": math.exp,
            "pi": math.pi,
            "e": math.e,
            "factorial": math.factorial,
            "degrees": math.degrees,
            "radians": math.radians,
        }
        
        result = eval(expression, safe_dict)
        calc.add_to_history(expression, result)
        return result
        
    except Exception as e:
        raise ValueError(f"Invalid expression: {e}")


def main():
    """Main calculator program"""
    calc = Calculator()
    
    print("Welcome to the Advanced Calculator!")
    print("Perfect for TCAD simulations and scientific calculations.")
    
    while True:
        print_menu()
        
        try:
            choice = input("\nEnter your choice (0-19): ").strip()
            
            if choice == '0':
                print("Thank you for using the calculator!")
                break
                
            elif choice == '1':  # Addition
                a = get_number("Enter first number: ")
                b = get_number("Enter second number: ")
                result = calc.add(a, b)
                operation = f"{a} + {b}"
                
            elif choice == '2':  # Subtraction
                a = get_number("Enter first number: ")
                b = get_number("Enter second number: ")
                result = calc.subtract(a, b)
                operation = f"{a} - {b}"
                
            elif choice == '3':  # Multiplication
                a = get_number("Enter first number: ")
                b = get_number("Enter second number: ")
                result = calc.multiply(a, b)
                operation = f"{a} * {b}"
                
            elif choice == '4':  # Division
                a = get_number("Enter dividend: ")
                b = get_number("Enter divisor: ")
                result = calc.divide(a, b)
                operation = f"{a} / {b}"
                
            elif choice == '5':  # Power
                base = get_number("Enter base: ")
                exponent = get_number("Enter exponent: ")
                result = calc.power(base, exponent)
                operation = f"{base} ^ {exponent}"
                
            elif choice == '6':  # Square Root
                x = get_number("Enter number: ")
                result = calc.square_root(x)
                operation = f"√{x}"
                
            elif choice == '7':  # Logarithm
                x = get_number("Enter number: ")
                base_choice = input("Enter base (default 10, 'e' for natural): ").strip()
                if base_choice.lower() == 'e':
                    result = calc.natural_log(x)
                    operation = f"ln({x})"
                elif base_choice == '':
                    result = calc.logarithm(x)
                    operation = f"log({x})"
                else:
                    base = float(base_choice)
                    result = calc.logarithm(x, base)
                    operation = f"log_{base}({x})"
                
            elif choice == '8':  # Natural Log
                x = get_number("Enter number: ")
                result = calc.natural_log(x)
                operation = f"ln({x})"
                
            elif choice == '9':  # Sine
                x = get_number("Enter angle: ")
                degrees = input("Is angle in degrees? (y/n): ").lower().startswith('y')
                result = calc.sin(x, degrees)
                unit = "°" if degrees else "rad"
                operation = f"sin({x}{unit})"
                
            elif choice == '10':  # Cosine
                x = get_number("Enter angle: ")
                degrees = input("Is angle in degrees? (y/n): ").lower().startswith('y')
                result = calc.cos(x, degrees)
                unit = "°" if degrees else "rad"
                operation = f"cos({x}{unit})"
                
            elif choice == '11':  # Tangent
                x = get_number("Enter angle: ")
                degrees = input("Is angle in degrees? (y/n): ").lower().startswith('y')
                result = calc.tan(x, degrees)
                unit = "°" if degrees else "rad"
                operation = f"tan({x}{unit})"
                
            elif choice == '12':  # Factorial
                n = int(get_number("Enter integer: "))
                result = calc.factorial(n)
                operation = f"{n}!"
                
            elif choice == '13':  # Percentage
                value = get_number("Enter value: ")
                percent = get_number("Enter percentage: ")
                result = calc.percentage(value, percent)
                operation = f"{percent}% of {value}"
                
            elif choice == '14':  # Memory Store
                value = get_number("Enter value to store: ")
                result = calc.memory_store(value)
                print(result)
                continue
                
            elif choice == '15':  # Memory Recall
                result = calc.memory_recall()
                print(f"Memory: {result}")
                continue
                
            elif choice == '16':  # Memory Clear
                result = calc.memory_clear()
                print(result)
                continue
                
            elif choice == '17':  # Show History
                history = calc.show_history()
                print(f"\nCalculation History:\n{history}")
                continue
                
            elif choice == '18':  # Clear History
                result = calc.clear_history()
                print(result)
                continue
                
            elif choice == '19':  # Expression Calculator
                expression = input("Enter mathematical expression: ")
                result = evaluate_expression(expression, calc)
                print(f"Result: {result}")
                continue
                
            else:
                print("Invalid choice. Please try again.")
                continue
            
            # Display result and add to history
            print(f"Result: {result}")
            calc.add_to_history(operation, result)
            
        except ValueError as e:
            print(f"Error: {e}")
        except KeyboardInterrupt:
            print("\n\nCalculator interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()