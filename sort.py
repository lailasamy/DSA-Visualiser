def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        yield arr

def merge_sort(arr):
    def merge(left, right):
        result = []
        while left and right:
            if left[0] < right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        result.extend(left or right)
        return result

    def merge_sort_recursive(array):
        if len(array) <= 1:
            return array
        mid = len(array) // 2
        left = merge_sort_recursive(array[:mid])
        right = merge_sort_recursive(array[mid:])
        merged = merge(left, right)
        return merged

    sorted_arr = merge_sort_recursive(arr)
    yield sorted_arr

def quicksort(arr):
    if len(arr) <= 1:
        yield arr
        return

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    yield from quicksort(left)
    yield middle
    yield from quicksort(right)

def counting_sort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)
    for num in arr:
        count[num] += 1
    index = 0
    for i, cnt in enumerate(count):
        while cnt > 0:
            arr[index] = i
            yield arr
            index += 1
            cnt -= 1

def radix_sort(arr):
    def counting_sort_by_digit(arr, exp):
        n = len(arr)
        output = [0] * n
        count = [0] * 10

        for i in range(n):
            index = (arr[i] // exp) % 10
            count[index] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        i = n - 1
        while i >= 0:
            index = (arr[i] // exp) % 10
            output[count[index] - 1] = arr[i]
            count[index] -= 1
            i -= 1

        for i in range(n):
            arr[i] = output[i]
            yield arr

    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        yield from counting_sort_by_digit(arr, exp)
        exp *= 10
