print("Enter the two numbers you want to perform the operation on below.\n")
first_number = int(input("First Number: "))
second_number = int(input("Second Number: "))
operator = int(input("Choose an operator from the list below by entering the corresponding number.\n1. *\n2. /\n3. +\n4. -\nChoice = "))

if operator == 1:
    result = first_number * second_number
    print(f"\n{first_number} * {second_number} = {result}")
elif operator == 2:
    result = first_number / second_number
    print(f"\n{first_number} / {second_number} = {result}")
elif operator == 3:
    result = first_number + second_number
    print(f"\n{first_number} + {second_number} = {result}")
elif operator == 4:
    result = first_number - second_number
    print(f"\n{first_number} - {second_number} = {result}")
else:
    print("Operator not recognised.")

exit = input("\nWill you like to continue?\n").lower()
if exit == "no":
    done = True
elif exit == "yes":
    done = False

answer = {
    "operation_answer": result
}

while not done:
    second_digit = int(input("\nEnter number: "))
    operator = int(input("Choose an operator from the list below\n1. *\n2. /\n3. +\n4. -\nChoice = "))
    if operator == 1:
        result = answer["operation_answer"] * second_digit
        print (f"\n{answer["operation_answer"]} * {second_digit} = {result}")
    elif operator == 2:
        result = answer["operation_answer"] / second_digit
        print (f"\n{answer["operation_answer"]} / {second_digit} = {result}")
    elif operator == 3:
        result = answer["operation_answer"] + second_digit
        print (f"\n{answer["operation_answer"]} + {second_digit} = {result}")
    elif operator == 4:
        result = answer["operation_answer"] - second_digit
        print(f"\n{answer["operation_answer"]} - {second_digit} = {result}")
    else:
        print("Operator not recognised.")

    answer["operation_answer"] = result
    exit = input("Will you like to continue?\n").lower()
    if exit == "no":
        done = True
    elif exit == "yes":
        done = False

#the program will be able to access previous calculations
