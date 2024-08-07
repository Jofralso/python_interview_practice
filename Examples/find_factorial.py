def find_factorial(n: int) -> int:
    if n == 0:
        return 1
    else:
        return n * find_factorial(n-1)
    

print(find_factorial(5))
print(find_factorial(10))
print(find_factorial(20))
