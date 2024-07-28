def partition(numbers, start, end):
    middle_element = numbers[end]
    middle_index = start

    for index in range(start, len(numbers)):
        if numbers[index] < middle_element:
            temp = numbers[index]
            numbers[index] = numbers[middle_index]
            numbers[middle_index] = temp
            middle_index += 1

    temp = numbers[middle_index]
    numbers[middle_index] = middle_element
    numbers[end] = temp

    return middle_index


def quick_sort(numbers, start, end):
    if start < end:
        pivot = partition(numbers, start, end)
        quick_sort(numbers, start, pivot - 1)
        quick_sort(numbers, start + 1, end)


elements = [10, 9, 8, 7, 6, 6, 5, 4, 3, 2, 1]
upper_bound = len(elements) - 1
print(elements)
print("----------------------------------")
quick_sort(elements, 0, upper_bound)
print(elements)
