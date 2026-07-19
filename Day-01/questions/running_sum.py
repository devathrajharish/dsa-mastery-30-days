def process_array(nums):
    """
    Process each element in an array
    Time: O(n)
    Space: O(1)
    """
    current_sum = 0
    result = []
    for num in nums:
        current_sum += num
        result.append(current_sum)
        
    return result
if __name__ == "__main__":
    nums = [1,2,3,4]
    print(process_array(nums)) 