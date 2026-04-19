def visualize_sequence(nums):
    nums = sorted(set(nums))
    print("\nSequence Visualization:")

    sequence = []
    for i in range(len(nums)):
        if i == 0 or nums[i] == nums[i-1] + 1:
            sequence.append(nums[i])
        else:
            print(sequence)
            sequence = [nums[i]]

    if sequence:
        print(sequence)
