# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index

        # One pass from cur_index to the value before the last one of the array
        # try to find index of the smallest element
        for j in range(i + 1, len(arr)):
            if arr[smallest_index] > arr[j]:
               smallest_index = j

        # swap value at cur_index with the smallest element found at smallest_index
        if smallest_index != cur_index:
            arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    swaps = True
    while swaps == True:

        # no swaps yet at the beginning
        swaps = False

        # One pass and swap adjacent values if necessary
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swaps = True

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    # count array size chosen from looking at the elements in the testing file
    count = [0] * 200

    #Better solution
    #if maximun == -1
    #maximun = max(arr)
    #count = [0] * maximum

    # count frequency of a number and save it in count array
    for num in arr:
        if num < 0:
            return "Error, negative numbers not allowed in Count Sort"
        else:
            count[num] += 1

    # clear original array and reset its size to 0 to append new sorted values
    arr.clear()

    for i in range(len(count)):
        num = count[i]
        if num != 0:
            arr.extend([i]*num)
    return arr
