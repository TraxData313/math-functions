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