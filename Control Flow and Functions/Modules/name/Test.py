import calculator

print("Now using calculator functions:")
print("10 + 20 =", calculator.add(10, 20))
# Use if __name__ == "__main__": when writing a file that can both run directly and be imported safely.
# It prevents unwanted code execution when importing.
# It’s essential for multiprocessing and package entry points.
