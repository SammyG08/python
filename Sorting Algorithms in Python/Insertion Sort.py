def insertion_sort(values):
    for index in range(1, len(values)):
        temp = values[index]
        empty_space = index
        while values[empty_space - 1] > temp and empty_space > 0:
            values[empty_space] = values[empty_space - 1]
            values[empty_space - 1] = temp
            empty_space -= 1


numbers = [10, 9, 8, 7, 6, 6, 5, 4, 3, 2, 1]

print(numbers)
print("----------------------------------")
insertion_sort(numbers)
print(numbers)
