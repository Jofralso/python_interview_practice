def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
def fibonacci_2(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
    
print(fibonacci(6))
print(fibonacci(5))
print(fibonacci(20))

print(fibonacci_2(6))
print(fibonacci_2(5))
print(fibonacci_2(20))
