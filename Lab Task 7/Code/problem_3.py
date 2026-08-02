my_list = [10, 20, 30, 40, 50]
print("List:", my_list)

try:
    index = input("Enter index to access: ")

    if not index.lstrip('-').isdigit():
        raise TypeError("Index must be an integer")

    index = int(index)
    print("Value at index", index, "is:", my_list[index])

except IndexError:
    print("IndexError: Index is out of range")
except TypeError as e:
    print("TypeError:", e)