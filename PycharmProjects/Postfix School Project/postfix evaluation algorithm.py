import os
def evaluation(expression):
    for character in expression:
        if character.isdigit():
            result.append(character)
        else:
            if(len(result) != 0):
                second_operand = int(result.pop())
                first_operand = int(result.pop())
                if character == "*":
                    result.append(first_operand * second_operand)
                elif character == "+":
                    result.append(first_operand + second_operand)
                elif character == "-":
                    result.append(first_operand - second_operand)
                elif character == "/":
                    result.append(first_operand / second_operand)
    if len(result) != 0:
        return result.pop()
    else:
        return("Invalid")


def receive_postfix_expression():
    os.system("color 7c")
    expression_to_evaluate = []
    done = False
    while not done:
        variable_in_expression = input("\n\n\n\n\n\n                                        Enter an operand or operator in the postfix expression.\n                                        Operator/Operand: ")
        expression_to_evaluate.append(variable_in_expression)
        user_response = input("\n                                           Done?\n                                         User Response: ").lower()
        if user_response == "yes":
            done = True
        os.system("cls")
    return expression_to_evaluate

os.system("color 7c")
result = []
postfix_expression_to_evaluate = receive_postfix_expression()
print("\n\n\n\n\n\n                                       Postfix Expression = ", end="")
for i in postfix_expression_to_evaluate:
    print(i, end=" ")
if (evaluation(postfix_expression_to_evaluate) != "Invalid"):
    print(f"\n\n                                       Result of postfix expression = {evaluation(postfix_expression_to_evaluate)}. \n\n\n\n\n\n\n\n\n")
else:
    print("\n\n                                     Invalid expression. \n\n\n\n\n\n\n\n\n")
del result
