def bubble_sort(values):
    for index in range(0, len(values)):
        for next_element_index in range(1, len(values) - index):
            if values[next_element_index - 1] > values[next_element_index]:
                temp = values[next_element_index - 1]
                values[next_element_index - 1] = values[next_element_index]
                values[next_element_index] = temp


numbers = [10, 9, 8, 7, 6, 6, 5, 4, 3, 2, 1]

print(numbers)
print("----------------------------------")
bubble_sort(numbers)
print(numbers)
