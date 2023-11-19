# It is easy to merge two sorted arrays. Hence, let's first implement the merge function
def merge(x, y):
    i, j = 0, 0
    merged = []
    while i<len(x) or j<len(y):
        if x[i]<y[j]:
            merged.append(x[i])
            if i+1<len(x):
                i += 1
            else:
                merged.extend(y[j:])
                break
        else:
            merged.append(y[j])
            if j+1<len(y):
                j += 1
            else:
                merged.extend(x[i:])
                break
    return merged

# A simple recursion that sorts any array
# Note: Python has a recursion limit and it's needed to be changed in order to work with bigger data
def merge_sort(ls: list[int]) -> list[int]:
    if len(ls) <= 1:
        return ls

    left = merge_sort(ls[:len(ls)//2])
    right = merge_sort(ls[len(ls)//2:])
    return merge(left, right)
