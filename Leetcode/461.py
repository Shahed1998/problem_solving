# The Hamming distance between two integers 
# is the number of positions at which the corresponding bits are different.

def hammingDistance(x, y):

    x = str(bin(x))[2:]
    y = str(bin(y))[2:]
    count = 0

    if len(x) > len(y):

        for i in range(len(x)-len(y)):
            y = '0' + y

    elif len(y) > len(x):
    
        for i in range(len(y)-len(x)):
            x = '0' + x

    for i,j in enumerate(x):

        if j != y[i]: count += 1

    return count

print(hammingDistance(3, 1))
