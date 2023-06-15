'''Program X - Consider the marks of 5 subjects obtained from user input.
Calculate the grade based on the criteria: >=90-A, >=80-B, >=70-C, >=60-D, >=50-E, <50-F.
Also find the result of student whether pass,promoted or detained given the criteria
5 subjects cleared-pass, >=3-promoted, <3-detained.
Perform necessary validations on marks such as negative marks, non-numeric marks.
Finally display student name, rollno, total marks and grade.
Implement the program using class'''
class Student:
    def __init__(self):
        self.__roll = 0
        self.__name = ""
        self.__marks = []
        self.__total = 0
        self.__per = 0
        self.__grade = ""
        self.__result = ""

    def setStudent(self):
        self.__roll = int(input("Enter Roll: "))
        self.__name = input("Enter Name: ")
        print("Enter marks of 5 subjects: ")
        for i in range(5):
            self.__marks.append(int(input("Subject " + str(i + 1) + ": ")))

    def calculateTotal(self):
        for x in self.__marks:
            self.__total += x

    def calculatePercentage(self):
        self.__per = self.__total / 5

    def calculateGrade(self):
        if self.__per >= 85:
            self.__grade = "S"
        elif self.__per >= 75:
            self.__grade = "A"
        elif self.__per >= 65:
            self.__grade = "B"
        elif self.__per >= 55:
            self.__grade = "C"
        elif self.__per >= 50:
            self.__grade = "D"
        else:
            self.__grade = "F"

    def calculateResult(self):
        count = 0
        for x in self.__marks:
            if x >= 50:
                count += 1
        if count == 5:
            self.__result = "PASSED"
        elif count >= 3:
            self.__result = "PROMOTED"
        else:
            self.__result = "DETAINED"

    def showStudent(self):
        self.calculateTotal()
        self.calculatePercentage()
        self.calculateGrade()
        self.calculateResult()
        print(self.__roll, "\t\t", self.__name, "\t\t", self.__total, "\t\t", self.__per, "\t\t", self.__grade, "\t\t",
              self.__result)


def main():
    # Student object
    s = Student()
    s.setStudent()
    s.showStudent()


if __name__ == "__main__":
    main()
