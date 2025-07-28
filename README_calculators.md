# Python Calculator Suite

This repository contains two comprehensive Python calculators: a command-line version and a GUI version. Both calculators support basic arithmetic operations and advanced scientific functions, making them perfect for TCAD simulations and general scientific calculations.

## Features

### Basic Operations
- Addition (+)
- Subtraction (-)
- Multiplication (*)
- Division (/)
- Exponentiation (^)
- Square Root (√)

### Scientific Functions
- Trigonometric functions (sin, cos, tan) with degree/radian support
- Logarithmic functions (log base 10, natural log)
- Mathematical constants (π, e)
- Factorial calculations
- Percentage calculations

### Additional Features
- Memory functions (store, recall, clear)
- Calculation history
- Expression evaluator (GUI version includes basic expression parsing)
- Error handling for invalid operations
- User-friendly interface

## Files

### 1. `calculator.py` - Command-Line Calculator
A full-featured command-line calculator with an interactive menu system.

**Features:**
- Menu-driven interface with 19 different operations
- Expression calculator for complex mathematical expressions
- Memory functions
- Calculation history (shows last 10 calculations)
- Comprehensive error handling
- Support for both degrees and radians in trigonometric functions

**Usage:**
```bash
python3 calculator.py
```

### 2. `calculator_gui.py` - GUI Calculator
A graphical calculator built with tkinter, providing a familiar calculator interface.

**Features:**
- Modern GUI with button layout similar to standard calculators
- Scientific function buttons
- Memory indicator
- History viewer in popup window
- Constants (π, e) easily accessible
- Real-time calculation display
- Error messages via popup dialogs

**Usage:**
```bash
python3 calculator_gui.py
```

**Note:** Requires a display environment. The GUI calculator needs X11 forwarding if running on a remote server.

## Installation and Requirements

### Prerequisites
- Python 3.x
- tkinter (for GUI version)

### Installing tkinter (if not already installed)
```bash
# Ubuntu/Debian
sudo apt-get install python3-tk

# CentOS/RHEL/Fedora
sudo yum install tkinter
# or
sudo dnf install python3-tkinter

# macOS (with Homebrew)
brew install python-tk

# Windows
# tkinter comes pre-installed with Python on Windows
```

### No Additional Python Packages Required
Both calculators use only Python standard library modules:
- `math` - for mathematical functions
- `sys` - for system operations
- `tkinter` - for GUI (built-in on most Python installations)

## Example Usage

### Command-Line Calculator
```bash
$ python3 calculator.py
Welcome to the Advanced Calculator!
Perfect for TCAD simulations and scientific calculations.

==================================================
           ADVANCED CALCULATOR
==================================================
Basic Operations:
  1. Addition (+)
  2. Subtraction (-)
  3. Multiplication (*)
  4. Division (/)
  5. Power (^)
  6. Square Root (√)

Scientific Functions:
  7. Logarithm (log)
  8. Natural Log (ln)
  9. Sine (sin)
 10. Cosine (cos)
 11. Tangent (tan)
 12. Factorial (!)
 13. Percentage (%)

Memory Functions:
 14. Memory Store (MS)
 15. Memory Recall (MR)
 16. Memory Clear (MC)

Utility:
 17. Show History
 18. Clear History
 19. Expression Calculator
  0. Exit
==================================================

Enter your choice (0-19): 19
Enter mathematical expression: 2*pi*sqrt(16)
Result: 25.132741228718345
```

### GUI Calculator
The GUI calculator provides an intuitive point-and-click interface with:
- Number pad (0-9)
- Basic operators (+, -, ×, ÷)
- Scientific functions (sin, cos, tan, log, ln, √, x²)
- Memory buttons (MC, MR, MS)
- Constants (π, e)
- History viewer

## Calculator Class Usage

You can also import and use the Calculator class directly in your Python code:

```python
from calculator import Calculator

calc = Calculator()

# Basic operations
result = calc.add(5, 3)          # 8
result = calc.multiply(4, 7)     # 28
result = calc.divide(15, 3)      # 5.0

# Scientific functions
result = calc.sin(30, degrees=True)    # 0.5 (30 degrees)
result = calc.logarithm(100)           # 2.0 (log base 10)
result = calc.square_root(16)          # 4.0

# Memory operations
calc.memory_store(42)
value = calc.memory_recall()     # 42

# History
calc.add_to_history("2+2", 4)
history = calc.show_history()
```

## Error Handling

Both calculators include comprehensive error handling for:
- Division by zero
- Invalid mathematical operations (e.g., √(-1), log(0))
- Invalid input types
- Overflow errors

## Use Cases

These calculators are particularly useful for:
- **TCAD Simulations**: Quick calculations during device modeling
- **Scientific Computing**: Basic to intermediate mathematical operations
- **Educational Purposes**: Learning Python programming and mathematical functions
- **General Purpose**: Daily calculations with scientific function support

## Tips

1. **Command-Line Calculator**: Use option 19 (Expression Calculator) for complex expressions like `sin(45*pi/180) + log10(100)`
2. **GUI Calculator**: The history button shows your last 20 calculations
3. **Memory Functions**: Store intermediate results for complex calculations
4. **Trigonometric Functions**: Remember to specify degrees vs radians when using trig functions

## Contributing

Feel free to extend these calculators with additional features such as:
- Complex number support
- Matrix operations
- Unit conversions
- Graphing capabilities
- More advanced scientific functions

## License

These calculators are provided as-is for educational and practical use.