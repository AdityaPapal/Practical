def greedy_selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Find the index of the minimum element in the unsorted part
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the minimum element with the first element of the unsorted part
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# Example usage:
unsorted_list = [64, 25, 12, 22, 11]
print("unsorted list:",unsorted_list)
sorted_list = greedy_selection_sort(unsorted_list)
print("Sorted list:", sorted_list)
