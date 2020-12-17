def mergeSortedArrays(arr1, arr2):
    finalArr = []
    i, j = 0, 0
    if len(arr1) == 0:
        return arr2
    if len(arr2) == 0:
        return arr1
    arr1ele = arr1[0]
    arr2ele = arr2[0]
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            finalArr.append(arr1[i])
            i += 1
        else:
            finalArr.append(arr2[j])
            j += 1

    if len(arr1) - i == 0:
        finalArr.extend(arr2[j:])
    else:
        finalArr.extend(arr1[i:])

    return finalArr


print(mergeSortedArrays([4, 6, 9, 13], []))

