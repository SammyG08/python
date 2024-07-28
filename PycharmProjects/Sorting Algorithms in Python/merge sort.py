def merge_sort(array, start, end):
    if start < end:
        middle = (start + end) // 2
        merge_sort(array, start, middle)
        merge_sort(array, middle + 1, end)
        merge(array, start, middle, end)


def merge(array, lowerbound, middle, upperbound):
    i = lowerbound
    j = middle + 1
    numbers = []
    while i <= middle and j <= upperbound:
        if array[i] > array[j]:
            numbers.append(array[j])
            j += 1
        elif array[i] <= array[j]:
            numbers.append(array[i])
            i += 1
    if i > middle:
        while j <= upperbound:
            numbers.append(array[j])
            j += 1
    if j > upperbound:
        while i < middle:
            numbers.append(array[i])
            i += 1
    for values_index in range(0,  len(numbers)):
        array[values_index] = numbers[values_index]


list_of_numbers = [10,5,3,2,6,7,9,8,1,4]
merge_sort(list_of_numbers, 0, 9)
print(list_of_numbers)

