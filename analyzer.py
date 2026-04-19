def longest_consecutive(nums):
    num_set = set(nums)
    longest = 0

    for num in num_set:
        if num - 1 not in num_set:
            current = num
            length = 1

            while current + 1 in num_set:
                current += 1
                length += 1

            longest = max(longest, length)

    return longest


def find_duplicates(nums):
    seen = set()
    duplicates = set()

    for num in nums:
        if num in seen:
            duplicates.add(num)
        seen.add(num)

    return list(duplicates)


def analyze_array(nums):
    return {
        "longest_consecutive": longest_consecutive(nums),
        "duplicates": find_duplicates(nums),
        "length": len(nums),
        "sum": sum(nums)
    }
