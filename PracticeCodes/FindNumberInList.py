if __name__ == "__main__":
    # Find if a particular value is present or not.
    list1 = [12, 33, 45, 67, 89, 100, 478, 567, 678, 890]
    value = int(input("enter the number to confirm whether it is present or not:"))
    if value in list1:
        print(value)
    else:
        print("Value is not present in list1")

    # Find if a particular value is present or not using for loop.
    for x in list1:
        if value == x:
            print(value)
            break
    else:
        print("no value")

    # Find if a particular value is present or not Using for loop based on index.

    for x in range(len(list1)):
        if list1[x] == value:
            print(value)
            break
    else:
        print("not value present in list1")
