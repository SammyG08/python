def postfix_algorithm(postfix_expression):
    for character in postfix_expression:
        if character.isdigit():
            result.append(character)
        else:
            second_operand = result.pop()
            first_operand = result.pop()
            if character == '*':
                result.append(int(first_operand) * int(second_operand))
            elif character == '+':
                result.append(int(first_operand) + int(second_operand))
            elif character == '-':
                result.append(int(first_operand) - int(second_operand))
            elif character == '/':
                result.append(int(first_operand) / int(second_operand))

    return result.pop()


result = []
expression = ("12", "10", "7", "+", "-", "3", "*")
print(f"Result is : {postfix_algorithm(expression)}.")
del result



