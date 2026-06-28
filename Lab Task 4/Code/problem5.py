def new_replace_value(lst, old_value, new_value):
    for i in range(len(lst)):
        if lst[i] == old_value:
            lst[i] = new_value
    return lst

sample_list = [10, 20, 30, 20, 50]
result = new_replace_value(sample_list, 20, 200)
print(result)