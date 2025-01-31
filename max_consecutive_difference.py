def max_consecutive_difference(lst):
 """
    Finds the maximum difference between consecutive elements in a list.
    
    Parameters:
    lst (list): The input list of numbers.
    
    Returns:
    int: The maximum consecutive difference.
  """
    if len(lst) < 2:
        return 0  # No consecutive difference possible
    
    return max(abs(lst[i+1] - lst[i]) for i in range(len(lst) - 1))
