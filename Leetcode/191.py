# The function takes an unsigned integer
# Converts it to binary, then further converts it to string
# then loops through the string and increases ones when one is found 

# Hamming Weight: Number of non zero symbols in a string

def hammingWeight(n):

    n = str(bin(n))

    ones = 0

    for i in n:

        if i == '1': ones += 1

    return ones

print(hammingWeight(128))