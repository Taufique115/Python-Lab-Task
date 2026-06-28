def remove_duplicates(lst):
    result = []

    for item in lst:
        if item not in result:
            result.append(item)

    return result

sample_list = [10, 20, 30, 20, 50]
print(remove_duplicates(sample_list))