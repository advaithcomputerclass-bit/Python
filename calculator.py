class Calculator:
    """
    A comprehensive calculator class that supports basic arithmetic operations,
    advanced mathematical functions, and expression evaluation with proper operator precedence.
    """

    def __init__(self):
        self.memory = 0
        self.history = []

    def add(self, a, b):
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result

    def subtract(self, a, b):
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result

    def multiply(self, a, b):
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result

    def power(self, base, exponent):
        result = base ** exponent
        self.history.append(f"{base} ^ {exponent} = {result}")
        return result

    def sqrt(self, x):
        if x < 0:
            raise ValueError("Square root of negative number is not allowed.")
        import math
        result = math.sqrt(x)
        self.history.append(f"sqrt({x}) = {result}")
        return result

    def sin(self, x):
        import math
        result = math.sin(math.radians(x))
        self.history.append(f"sin({x}) = {result}")
        return result

    def cos(self, x):
        import math
        result = math.cos(math.radians(x))
        self.history.append(f"cos({x}) = {result}")
        return result

    def tan(self, x):
        import math
        result = math.tan(math.radians(x))
        self.history.append(f"tan({x}) = {result}")
        return result

    def log(self, x, base=10):
        if x <= 0:
            raise ValueError("Logarithm of non-positive number is not allowed.")
        import math
        result = math.log(x, base)
        self.history.append(f"log{base}({x}) = {result}")
        return result

    def factorial(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("Factorial is only defined for non-negative integers.")
        import math
        result = math.factorial(n)
        self.history.append(f"{n}! = {result}")
        return result

    def evaluate_expression(self, expression):
        """
        Evaluate a mathematical expression with proper operator precedence.
        Supports +, -, *, /, ^, (, ), and functions like sin, cos, etc.
        """
        try:
            # Replace ^ with ** for power
            expression = expression.replace('^', '**')
            # Use eval with restricted globals for safety
            allowed_names = {
                "sin": self.sin,
                "cos": self.cos,
                "tan": self.tan,
                "sqrt": self.sqrt,
                "log": self.log,
                "fact": self.factorial,
                "__builtins__": {}
            }
            result = eval(expression, allowed_names)
            self.history.append(f"{expression} = {result}")
            return result
        except Exception as e:
            raise ValueError(f"Invalid expression: {str(e)}")

    def store_memory(self, value):
        self.memory = value

    def recall_memory(self):
        return self.memory

    def clear_history(self):
        self.history = []

    def get_history(self):
        return self.history.copy()


def main():
    calc = Calculator()
    print("Advanced Calculator")
    print("Commands:")
    print("  <expression> - evaluate expression (e.g., 2 + 3 * 4, sin(30), 5^2)")
    print("  mem <value> - store value in memory")
    print("  rec - recall memory")
    print("  hist - show history")
    print("  clear - clear history")
    print("  quit - exit")

    while True:
        try:
            user_input = input(">>> ").strip()
            if user_input.lower() == 'quit':
                break
            elif user_input.lower() == 'hist':
                for entry in calc.get_history():
                    print(entry)
            elif user_input.lower() == 'clear':
                calc.clear_history()
                print("History cleared.")
            elif user_input.lower().startswith('mem '):
                value = float(user_input[4:])
                calc.store_memory(value)
                print(f"Stored {value} in memory.")
            elif user_input.lower() == 'rec':
                print(f"Memory: {calc.recall_memory()}")
            else:
                result = calc.evaluate_expression(user_input)
                print(f"Result: {result}")
        except ValueError as e:
            print(f"Error: {e}")
        except KeyboardInterrupt:
            break


if __name__ == "__main__":
    main()