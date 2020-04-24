# Function
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