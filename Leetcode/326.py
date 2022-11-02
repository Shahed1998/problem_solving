def isPowerOfThree(n):
    
    if n == 1: return True

    elif n < 1: return False

    return isPowerOfThree(n/3)

print(isPowerOfThree(0))