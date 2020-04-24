'''
# Original function MVP, this one uses division of a product of all to find our results
# Below we have a version that don't use division!
def SpecialArrayProduct(array):
    # prod_all_arr: value for the product of all elements of the array
    prod_all_arr = 1
    for value in array:
        prod_all_arr = prod_all_arr * value
    
    # Recompose array
    array_new = list()
    for value in array:
        array_new.append(prod_all_arr / value)
        
    # Output
    return array_new
'''

'''
# Follow-up: what if you can't use division?
'''
def SpecialArrayProduct(array):
    # Creation of new array that is going to hold out output
    array_new = list()
    
    for value in array:
        # Create new array without value
        array_local = array.copy()
        array_local.remove(value)
        
        # Find the product of this array
        prod_all_arr = 1
        for value_local in array_local:
            prod_all_arr = prod_all_arr * value_local
        
        # Append product to our output array and move onto next iteration
        array_new.append(prod_all_arr)
        
    return array_new