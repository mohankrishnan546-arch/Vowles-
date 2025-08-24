def reverse(x):
    sign = -1 if x < 0 else 1
    x_abs = abs(x)
    rev = 0

    while x_abs != 0:
        pop = x_abs % 10
        x_abs //= 10
        rev = rev * 10 + pop

    rev *= sign

    # Check for 32-bit signed integer overflow
    if rev < -2**31 or rev > 2**31 - 1:
        return 0
    return rev
  
