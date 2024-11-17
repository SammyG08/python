def selection_sort(values):
    for index in range(0, len(values)):
        smallest_number_index = index
        for next_index in range(index + 1, len(values)):
            if values[smallest_number_index] > values[next_index]:
                smallest_number_index = next_index

        second_temp = values[index]
        values[index] = values[smallest_number_index]
        values[smallest_number_index] = second_temp


numbers = [10, 9, 8, 7, 6, 6, 5, 4, 3, 2, 1]

print(numbers)
print("----------------------------------")
selection_sort(numbers)
print(numbers)
