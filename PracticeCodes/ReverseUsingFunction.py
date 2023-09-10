def reverselist():
    list1 = [5, 8, 10, 45, 34, 67, 89, 100]
    r = range(len(list1) - 1, -1, -1)
    for x in r:
        rorder = list1[x]
        print(rorder)


if __name__ == "__main__":
    reverselist()
