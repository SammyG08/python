
studentmarks = {
  
         "Maxwell" : 70,
         "Hilary" : 86,
         "Solomon" : 92,
         "Lawrence" : 80,
         "Gregory" : 88,
         "Kwesi" : 66,
         "Kojo" : 70,
         "Alfred" : 49
  
}

for key in studentmarks :
    if studentmarks[key] > 90:
        grade = "A+"
        studentmarks[key] = grade
    elif studentmarks[key] > 80 :
        grade = "A"
        studentmarks[key] = grade
    elif studentmarks[key] > 75:
        grade = "B+"
        studentmarks[key] = grade
    elif studentmarks[key] > 70:
        grade = "B"
        studentmarks[key] = grade
    elif studentmarks[key] > 65:
        grade = "C+"
        studentmarks[key] = grade
    elif studentmarks[key] > 60:
        grade = "C-"
        studentmarks[key] = grade
    elif studentmarks[key] > 50:
        grade = "D"
        studentmarks[key] = grade
    elif studentmarks[key] < 50:
        grade = "F"
        studentmarks[key] = grade

done = False

print(studentmarks)

"""
while not done:
    
  
    studentSearch = input("Enter the first name of the student whose grade you want to access. ")

    print(f"{studentSearch} had a {studentmarks[studentSearch]}")
    
    choice = input("Would you like to continue?\n")
    
    if choice == "no":
        done = True

"""