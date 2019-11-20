# Python math functions
- This math_utils module will group math functions I use for my projects in order to maximise consistency.

### Usage:
- Download the math_utils.py to the code folder and import it by:<br>
<i>import math_utils</i>
- For function info check the description below
- More function contend might be available if it has a sub-folder

### Dependencies:
- Numpy: <i>pip install numpy</i>


<hr>

## Functions:

#### c_map(user_input, in_min, in_max, out_min, out_max):
    The function remaps the input from one range to another, just like:
    https://www.arduino.cc/reference/en/language/functions/math/map/
    
    Example:
    Map percents to ratios. If used with those params:
    c_map(user_input=50, in_min=0, in_max=100, out_min=0, out_max=1)
    the function will return 0.5 (since 50% = 0.5)

#### standardize_array(array: list, out_min=-1, out_max=1):
    The function standardizes the array of numbers (squishes the numbers linearly between -1 and 1)
    
    Example:
    Array before the function: [-100, -50, 50, 100]
    Array after the function: [-1.0, -0.5, 0.5, 1.0]
#### sigmoid(input_value: float):
    Activation funcion: Standard sigmoid
    
    Returns: 1/(1 + np.exp(-input_value))
