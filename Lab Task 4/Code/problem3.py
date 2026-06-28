def find_max_min(lst):
    maximum = lst[0]
    minimum = lst[0]

    for item in lst:
        if item > maximum:
            maximum = item
        if item < minimum:
            minimum = item

    return maximum, minimum

numbers = [12, 45, 7, 89, 23, 1]
max_val, min_val = find_max_min(numbers)
print("Maximum:", max_val)
print("Minimum:", min_val)