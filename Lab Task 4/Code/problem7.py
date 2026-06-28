def count_matching_strings(lst):
    count = 0

    for word in lst:
        if len(word) >= 2 and word[0] == word[-1]:
            count += 1

    return count

sample_list = ['aca', 'xyz', 'aba', '1221']
print(count_matching_strings(sample_list))