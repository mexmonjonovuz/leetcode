def buble_sort(arr: list[int]) -> list[int]:
    for i in range(len(arr)):
        for j in range(1, len(arr) - i):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
    return arr


print(buble_sort([1, 2, 3, 1, 1, 2, 3, 5, 7, 8]))
