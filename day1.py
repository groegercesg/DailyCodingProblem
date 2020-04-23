
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
    # No applicable value found, return false
    return False            
'''

'''
One pass version of AddToK
'''
def AddToK(array, k):
    # Outer loop to get elements
    for element in array:
        # Difference, i.e. we find the value that we need for this statement to be true
        # and then search to see if it exists in the array
        Difference = k - element
        if Difference in array:
            # If this is the case return True
            return True
    # No applicable value found, return false
    return False
