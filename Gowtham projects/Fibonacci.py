def fibonacci_iterative(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]

# Example usage
n = 10
print(f"First {n} Fibonacci numbers (iterative): {fibonacci_iterative(n)}")

def fibonacci_recursive(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = fibonacci_recursive(n - 1)
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence

# Example usage
n = 10
print(f"First {n} Fibonacci numbers (recursive): {fibonacci_recursive(n)}")

def fibonacci_memoization(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = fibonacci_memoization(n - 1, memo)
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        memo[n] = fib_sequence
        return fib_sequence

# Example usage
n = 10
print(f"First {n} Fibonacci numbers (memoization): {fibonacci_memoization(n)}")
