# Linear Search


def linearSearch(array, x):
    for i in range(0, 9):
        if (array[i] == x):
            return i
    return -1


nums = [10, 30, 40, 45, 70, 80, 85, 90, 100]
x = 100
result = linearSearch(nums, x)
if(result == -1):
    print("ELEMENT NOTFOUND")
else:
    print("ELEMENT FOUND AT: ", result)

