def c_map(user_input, in_min, in_max, out_min, out_max):
    """The function remaps the input from one range to another, just like:
    https://www.arduino.cc/reference/en/language/functions/math/map/
    
    Example:
    Map percents to ratios. If used with those params:
    c_map(user_input=50, in_min=0, in_max=100, out_min=0, out_max=1)
    the function will return 0.5 (since 50% = 0.5)
    """
    
    # Calculate the ratio for the two ranges:
    in_range = in_max - in_min
    out_range = out_max - out_min
    range_ratio = out_range/in_range
    
    # Calculate how far is the input from in_min:
    input_dist_from_min = user_input - in_min
    
    # Calculate how far from out_min the output should be:
    output_dist_from_min = input_dist_from_min*range_ratio
    
    # Calculate and return the output:
    return out_min + output_dist_from_min  
    

def standardize_array(array: list, out_min=-1, out_max=1):
    """The function standardizes the array of numbers (squishes the numbers linearly between -1 and 1)
    
    Example:
    Array before the function: [-100, -50, 50, 100]
    Array after the function: [-1.0, -0.5, 0.5, 1.0]
    """
    in_min = np.min(array)
    in_max = np.max(array)
    for el in range(len(array)):
        array[el] = c_map(array[el], in_min, in_max, out_min, out_max)
        
    return array