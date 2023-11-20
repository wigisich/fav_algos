def binary_search(item, arr, pointer_low, pointer_high):
    if pointer_low <= pointer_high:
        mid = (pointer_low + pointer_high) // 2

        if arr[mid] == item:
            return mid
        elif arr[mid] < item:
            return binary_search(item, arr, mid + 1, pointer_high)
        else:
            return binary_search(item, arr, pointer_low, mid-1)
    else:
        return -1
