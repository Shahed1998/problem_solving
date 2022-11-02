def isPowerOfFour(n):

    if n == 1: return True

    elif n < 1: return False

    return isPowerOfFour(n/4)

print(isPowerOfFour(2))