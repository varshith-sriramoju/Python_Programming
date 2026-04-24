def add(a, b):
    return a + b

def sub(a, b):
    return a - b

print("Calculator module loaded!")

# Use if __name__ == "__main__": when writing a file that can both run directly and be imported safely.
# It prevents unwanted code execution when importing.
# It’s essential for multiprocessing and package entry points.

# This block runs ONLY if you run calculator.py directly
if __name__ == "__main__":
    print("Running calculator directly…")
    print("2 + 3 =", add(2, 3))
    print("7 - 4 =", sub(7, 4))
