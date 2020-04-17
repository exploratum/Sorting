# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    merged_arr = []

    while True:
        if not arrA or not arrB:
            break
        if arrA[0] < arrB[0]:
            merged_arr.append(arrA.pop(0))
        else:
            merged_arr.append(arrB.pop(0))
            

    if not arrA:
        merged_arr.extend(arrB)
    if not arrB:
        merged_arr.extend(arrA)

    return merged_arr

###########################################################################################################################################
#   Alternate solution for merge function to improve performance - avoid list shifting after popping at the begining - pop at end instead #
###########################################################################################################################################
def merge2( arrA, arrB ):

    merged_arr_length = len(arrA) + len(arrB)
    merged_arr = [0] * merged_arr_length

    
    for i in reversed(range(merged_arr_length)):
        if not arrA or not arrB:
            break
        if arrA[len(arrA) - 1] > arrB[len(arrB) - 1]:
            merged_arr[i] = arrA.pop()
        else:
            merged_arr[i] = arrB.pop()
            

    if not arrA:
        for i in range(0, len(arrB)):
            merged_arr[i] = arrB[i]

    if not arrB:
        for i in range(0, len(arrA)):
            merged_arr[i] = arrA[i]


    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    
    if len(arr) <= 1:
        return arr

    else:
        middle = len(arr)//2
        arrA = arr[0:middle]
        arrB = arr[middle:]

        mergedA = merge_sort(arrA)
        mergedB = merge_sort(arrB)

        arr = merge(mergedA, mergedB)
        return arr






####################################################################

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
