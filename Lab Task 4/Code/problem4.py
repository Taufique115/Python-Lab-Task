def linear_search(lst, target):
    for index in range(len(lst)):
        if lst[index] == target:
            return index
    return -1

numbers = [10, 25, 33, 47, 52]
target = 47
result = linear_search(numbers, target)

if result != -1:
    print(f"Found {target} at index {result}")
else:
    print(f"{target} not found")