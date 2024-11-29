def max_removals(main_string, substrings, count=0):
    max_count = count
    for substring in substrings:
        if substring in main_string:
            updated_string = main_string.replace(substring, "", 1)
            new_substrings = substrings.copy()
            new_substrings.remove(substring)
            max_count = max(max_count, max_removals(updated_string, new_substrings, count + 1))
    return max_count

# Read input
N = int(input().strip())  # Number of substrings
substrings = input().strip().split()  # List of substrings
main_string = input().strip()  # Main string

# Output the result
result = max_removals(main_string, substrings)
print(result)

# Time complexity: O(N * 2^N)