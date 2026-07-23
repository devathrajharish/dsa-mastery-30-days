def duplicates(lst):
    """
    This function checks if a list contains any duplicates.
    It returns True if duplicates are found, otherwise False.
    """
    # Example list to check for duplicates
    
    # Convert the list to a set to remove duplicates
    unique_elements = set(lst)

    # Compare the length of the original list with the set
    if len(lst) != len(unique_elements):
        return True  # Duplicates found
    else:
        return False  # No duplicates found

if __name__ == "__main__":
    sample_list = [1, 2, 3, 4, 5, 1]
    print(duplicates(sample_list))  # Output: True
