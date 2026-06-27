starts_with = lambda main_string, sub_string: main_string.startswith(sub_string)

main_string = input("Enter the main string: ")
sub_string = input("Enter the sub-string to check: ")

print(starts_with(main_string, sub_string))