def convert_base(a, b, n):
    # Step 1: Convert from base a to base 10
    decimal_number = int(n, a)
    
    # Step 2: Convert from base 10 to base b
    if decimal_number == 0:
        return "0"
    
    digits = []
    while decimal_number > 0:
        digits.append(str(decimal_number % b))
        decimal_number //= b
    
    # Since we get the digits in reverse order, reverse them
    return ''.join(digits[::-1])

# Input
a, b = map(int, input().strip().split())
n = input().strip()

# Output
print(convert_base(a, b, n))