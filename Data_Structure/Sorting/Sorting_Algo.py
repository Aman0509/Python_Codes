def bubble(arr):
    """
    In place and Stable Sorting method
    """
    print("Original - ", arr)
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        print(f"Iter {i+1} -> ", arr)
    return arr


def selection(arr):
    """
    In place and Unstable Sorting method
    """
    print("Original - ", arr)
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[j], arr[i] = arr[i], arr[j]
        print(f"Iter {i+1} -> ", arr)
    return arr


def insertion(arr):
    """
    In place and Stable Sorting method
    """
    print("Original - ", arr)
    for i in range(len(arr)-1):
        c = i + 1
        for j in range(c):
            if arr[j] > arr[c]:
                arr[c], arr[j] = arr[j], arr[c]
        print(f"Iter {c} -> ", arr)
    return arr


def merge(arr):
    """
    Out of place, Stable Sorting method
    It uses divide and conquer approach
    """
    if len(arr) > 1:
        mid_ind = len(arr)//2
        left_arr = arr[:mid_ind]
        right_arr = arr[mid_ind:]
        merge(left_arr)
        merge(right_arr)
        i = j = k = 0
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1


def quick(arr, low, high):
    """
    In place and Unstable Sorting method
    It uses divide and conquer approach
    """
    if low < high:
        k = partition(arr, low, high)
        quick(arr, low, k-1)
        quick(arr, k+1, high)


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1


def heap(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < n and arr[largest] < arr[l]:
        largest = l

    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Heapify the root.
        heapify(arr, n, largest)


if __name__ == '__main__':
    arr = [34, 23, 12, 9, 21, 87, 36, 29, 33]
    # print("Bubble Sort - ", bubble(arr))
    # print("Selection Sort - ", selection(arr))
    # print("Insertion Sort - ", insertion(arr))
    # merge(arr)
    # quick(arr, 0, len(arr)-1)
    # heap(arr)


