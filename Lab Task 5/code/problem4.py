def get_distinct(lst):
    distinct_list = []
    
    for item in lst:
        if item not in distinct_list:
            distinct_list.append(item)
    
    return distinct_list

user_input = input("Enter numbers separated by commas (e.g. 1,2,3,3,3,4,5): ")
sample_list = [int(x) for x in user_input.split(",")]

result = get_distinct(sample_list)
print("Distinct elements:", result)