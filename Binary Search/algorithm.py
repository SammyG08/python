def bs_algorithm(numbers, start, end, number):
    mid_index = (start + end) // 2
    middle_element = numbers[mid_index]
    if start <= end:
        if number > middle_element:
            return bs_algorithm(numbers, mid_index + 1, end, number)
        elif number < middle_element:
            return bs_algorithm(numbers, start, mid_index, number)
        elif number == middle_element:
            return mid_index
    else:
        return -1


list_of_numbers = [1, 5, 9, 10, 15, 19, 23,]
print(bs_algorithm(numbers=list_of_numbers, start=0, end=6, number=15))
