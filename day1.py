
'''
# This version isn't as good as it has BigO complexity of O^{2}(N)
# Which is polynomial and so an issue for large input lists 

def AddToK(array, k):
    # Outer loop for initial value
    for i in range(0, (len(array) - 1)):
        # Inner loop for second value
        for j in range((i + 1), len(array)):
            # Do two numbers from the list add up to k
            if (array[i] + array[j] == k):
                # If this is the case return True
                return True
'''

'''
One pass version of AddToK
'''

#Test