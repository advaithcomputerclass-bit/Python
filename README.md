# Advanced Calculator

A comprehensive Python calculator that supports basic arithmetic, advanced mathematical functions, and complex expression evaluation with proper operator precedence.

## Features

- Basic operations: addition, subtraction, multiplication, division
- Advanced functions: power, square root, trigonometric functions (sin, cos, tan), logarithm, factorial
- Expression evaluation with precedence (e.g., 2 + 3 * 4)
- Memory storage and recall
- Calculation history
- Error handling for invalid operations

## Usage

Run the calculator:

```bash
python calculator.py
```

### Commands

- `<expression>`: Evaluate a mathematical expression (e.g., `2 + 3 * 4`, `sin(30)`, `5^2`)
- `mem <value>`: Store a value in memory
- `rec`: Recall the value from memory
- `hist`: Display calculation history
- `clear`: Clear the history
- `quit`: Exit the calculator

### Examples

```
>>> 2 + 3
Result: 5
>>> sin(90)
Result: 1.0
>>> 5 ^ 2
Result: 25
>>> mem 42
Stored 42.0 in memory.
>>> rec
Memory: 42.0
>>> hist
2 + 3 = 5
sin(90) = 1.0
5 ^ 2 = 25
```

## Testing

Run the unit tests:

```bash
python test_calculator.py
```

## Requirements

- Python 3.x
- Standard library (math module)

## Troubleshooting

- **Division by zero**: The calculator prevents division by zero and raises a ValueError.
- **Invalid expressions**: Use proper syntax; the calculator will report errors for invalid input.
- **Negative square root**: Square root of negative numbers is not allowed.
- **Factorial**: Only defined for non-negative integers.

## License

This code is provided as-is for educational purposes.