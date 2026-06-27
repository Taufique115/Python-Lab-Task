def count_elements(lst):
    counts = {}
    
    for item in lst:
        if item in counts:
            counts[item] = counts[item] + 1
        else:
            counts[item] = 1
    
    for key, value in counts.items():
        print(f"{key} => {value}")

user_input = input("Enter numbers separated by commas (e.g. 10,20,30,30,30,30,20,40): ")
sample_list = [int(x) for x in user_input.split(",")]

count_elements(sample_list)