#LINEAR FUNCTION 

def linearSearch(array, item, num):

    for i in range(0, num):
        if (array[i] == item):
            return i
    return -1

#TEST INPUT
array1 = [2, 4, 0, 1, 9]
item1 = 4
num1 = len(array1)
result = linearSearch(array1, num1, item1)
if(result == -1):
    print("ITEM NOT FOUND")
else:
    print("ITEM FOUND AT", result)