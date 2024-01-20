def permute(nums):
    """
    Return all permutations of the given list.
    >>> permute([1, 2, 3])
    [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]]
    """
    global permutation_count  # Declare permutation_count as global

    def backtrack(start):
        """
        Generate permutations by recursively swapping elements.
        """
        global permutation_count  # Declare permutation_count as global
        if start == len(nums) - 1:
            output.append(nums[:])
            permutation_count += 1  # Use permutation_count here
        else:
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                # backtrack
                nums[start], nums[i] = nums[i], nums[start]

    output = []
    permutation_count = 0  # Initialize permutation_count
    backtrack(0)
    return output


# input the list from keyboard
while True:
    input_str = input("enter a list of numbers separated by commas: ")
    nums = [int(x) for x in input_str.split(',') if x.strip().isdigit()]

    if nums:
        break
    else:
        print("Invalid input. Please, try again.")

res = permute(nums)
#print(f"Permutations of the list {nums} are: {res}")
print(f"Total permutations: {permutation_count}")
