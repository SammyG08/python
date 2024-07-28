#Note when you use the super function you dont need to use the self keyword
class University:
    def __init__(self,university_name):
        self.university_name = university_name
        #print("Calling university constructor")

    def show_details(self):
        print(f"University: {self.university_name}")


class Course(University):
    def __init__(self, university_name, course_name):
        self.course_name = course_name
        University.__init__(self, university_name)
        #print("Calling course constructor")

    def show_details(self):
        University.show_details(self)
        print(f"Course name: {self.course_name}\n--------------------------------------")


class Branch(University):
    def __init__(self, university_name, branch_name):
        self.branch_name = branch_name
        University.__init__(self, university_name)
        #print("Calling branch constructor")

    def show_details(self):
        super().show_details()
        print(f"Branch name: {self.branch_name}\n--------------------------------------")


class Student(Course,Branch):
    def __init__(self,university_name, course_name, branch_name, student_name):
        Course.__init__(self, university_name, course_name)
        Branch.__init__(self, university_name, branch_name)
        self.student_name = student_name

    def show_details(self):
        #Course.show_details(self)
        #Branch.show_details(self)
        print(f"University name: {self.university_name}\nBranch name: {self.branch_name}\nCourse name: {self.course_name}\nStudent name: {self.student_name}\n--------------------------------------")


class Field(Branch):
    def __init__(self, university_name, branch_name, major_name):
        super().__init__(university_name, branch_name)
        self.major_name = major_name

    def show_details(self):
        #super().show_details()
        print(f"University name: {self.university_name}\nBranch name: {self.branch_name}\nMajor Field: {self.major_name}\n--------------------------------------")


print("\n\n")
course = Course("New York University", "Discrete Mathematics")
course.show_details()

branch = Branch("New York University", "Computer Science")
branch.show_details()

student_one = Student("New York University", "Discrete Mathematics", "Computer Science", "Sheryl Davies")
student_one.show_details()

student_field = Field("New York University", "Computer Science", "Software Engineering")
student_field.show_details()


