def quick_sort(arr, left=None, right=None):
    if left is None:
        left = 0
    if right is None:
        right = arr.__len__() - 1
    if left<right:
        # partition_index = partition_right(arr, left, right)
        # partition_index = partition_left(arr, left, right)
        partition_index = partition_mid(arr, left, right)

        quick_sort(arr, left, partition_index - 1)
        quick_sort(arr, partition_index + 1, right)

    return arr


def partition_left(arr, left, right):
    # 使用数组的第一个元素作为基准元素
    pivot = left
    # record the pivot index
    index = pivot + 1
    i = index
    while i <= right:
        if arr[i] < arr[pivot]:
            swap(arr, i, index)
            index += 1
        i += 1
    swap(arr, pivot, index - 1)
    return index - 1

def partition_right(arr, left, right):
    # 使用数组的最后一个元素作为基准元素
    pivot = right
    # record the pivot index
    index = pivot - 1
    j = index
    while j >= left:
        if arr[j] > arr[pivot]:
            swap(arr, j, index)
            index -= 1
        j -= 1
    swap(arr, pivot, index + 1)
    return index+1

def partition_mid(arr, left, right):
    # 使用数组的最后一个元素作为基准元素
    pivot = left + (right-left) // 2

    while left<=right:

        while arr[left]<arr[pivot]:
            left+=1
        while arr[right]>arr[pivot]:
            right-=1

        swap(arr, left, right)

        if left == pivot:
            pivot = right
            return pivot
        if right == pivot:
            pivot = left
            return pivot


        left+=1
        right-=1

    return pivot


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


# L1 = [27, 4, 5, 34, 5, 6, 24, 234, 534, 25]
# L2 = quick_sort(L1)
# print(L2)
L1 = [7,6,2,4, 5]
L2 = quick_sort(L1)
print(L2)
