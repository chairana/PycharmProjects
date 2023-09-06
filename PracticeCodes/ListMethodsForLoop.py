if __name__ == "__main__":
    arrayValues = [22,200, 1000, 200, -1, 1, 0, 500, 255,2000]
    # TODO: - write the code with out using the "min" and "max" methods.
    # TODO:- get the max value of the arrayValues using the for loop
    # Your Code

    # TODO: - Get the sum of the arrayValues using the for loop
    # Your code.
    # TODO: - Get the minimum values of the arrayValues using the for loop
    # Your code
    minvalue=arrayValues[0]
    for x in arrayValues:
        if x < minvalue:
            minvalue=x
    print(minvalue)

    sum=0
    for x in arrayValues:
        sum=sum+x
print(sum)










