def factorial1(n):
    if n == 0:
        return 1
    else:
        return n * factorial1(n-1)


# Example usage
n = int(input("Enter a number: "))

print(factorial1(n))  # Output: 120
