def twoSum(nums, target):
    lookup = {}

    for i,n in enumerate(nums):
        
        diff = target - n

        if diff in lookup:

            return [lookup[diff], i]

        lookup[n] = i
    
    return []



print(twoSum([3,3], 6))

