def calculate_lift_rounds(n, capacity):
    """
    Efficiently calculates the number of rounds the lift needs to cover.
    
    Parameters:
    n (int): Total number of people.
    capacity (int): Maximum number of people the lift can carry in one round.
    
    Returns:
    int: The number of rounds required to transport all people to the top floor.
    """
    # Calculate the number of full rounds
    full_rounds = n // capacity

    # Check if there are remaining people who need an additional round
    if n % capacity != 0:
        full_rounds += 1
    
    return full_rounds

# Example
print(calculate_lift_rounds(10, 3))  
print(calculate_lift_rounds(7, 4))   
