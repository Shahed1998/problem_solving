def isPowerOfTwo(n):

    if n == 1: return True

    elif n < 1: return False

    else: return isPowerOfTwo(n / 2)

print(isPowerOfTwo(8.5))