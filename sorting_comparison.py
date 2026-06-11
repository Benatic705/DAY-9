import time

numbers = [45, 12, 78, 23, 9, 56, 34, 67, 89, 1]

# Bubble Sort
def bubble_sort(arr):
    a = arr.copy()

    for i in range(len(a)):
        for j in range(len(a) - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

    return a


# Selection Sort
def selection_sort(arr):
    a = arr.copy()

    for i in range(len(a)):
        min_index = i

        for j in range(i + 1, len(a)):
            if a[j] < a[min_index]:
                min_index = j

        a[i], a[min_index] = a[min_index], a[i]

    return a


# Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    result = []

    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    result.extend(left)
    result.extend(right)

    return result


# Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]

    left = []
    right = []

    for i in arr[1:]:
        if i <= pivot:
            left.append(i)
        else:
            right.append(i)

    return quick_sort(left) + [pivot] + quick_sort(right)


print("Sorting Performance Comparison")
print()

start = time.time()
print("Bubble Sort:", bubble_sort(numbers))
print("Time:", time.time() - start)

print()

start = time.time()
print("Selection Sort:", selection_sort(numbers))
print("Time:", time.time() - start)

print()

start = time.time()
print("Merge Sort:", merge_sort(numbers))
print("Time:", time.time() - start)

print()

start = time.time()
print("Quick Sort:", quick_sort(numbers))
print("Time:", time.time() - start)