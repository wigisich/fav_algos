def binary_search(item, arr, pointer_low, pointer_high):
    # The use of pointers here play an important role.
    # Because, for example, if we try to declare them inside the recursion, it will create a new search space for each recursive call.
    # This would introduce an unnecessary complexity with the loss of the information about the index we currently are.

    if pointer_low <= pointer_high:                                 # Check the order of the pointers
        mid = (pointer_low + pointer_high) // 2

        if arr[mid] == item:
            return mid
        elif arr[mid] < item:
            return binary_search(item, arr, mid + 1, pointer_high)  # Take the second half for the recursion
        else:
            return binary_search(item, arr, pointer_low, mid-1)     # Take the first half for the recursion
    else:
        return -1                                                   # In case given pointers are incorrect
