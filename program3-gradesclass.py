'''Program 3 - Consider the marks of 5 subjects obtained from user input.
Calculate the grade based on the criteria: >=90-A, >=80-B, >=70-C, >=60-D, >=50-E, <50-F.
Perform necessary validations on marks such as negative marks, non-numeric marks.
Finally display student name, rollno, total marks and grade.
Implement the program using class'''
class student:
    def __init__(self):
        self.name=''
        self.roll=0
        self.marks=[]
        self.total=0
        self.avg=0.0
        self.grade=''

    def set(self):
        self.name=input('Enter name:')
        self.roll=input('Enter roll no:')
        for i in range(5):
            self.marks.append(int(input('Subject'+str(i+1)+' marks')))

    def computeavg(self):
        for i in range(5):
            if (self.marks[i]<0):
                print('Cant perform operation')
                quit()
        for i in range(5):
            self.total+=self.marks[i]
        self.avg=self.total/len(self.marks)

    def computegrade(self):
        for i in range(5):
            if (self.marks[i]<50):
                self.grade='Fail'

        if (self.avg >= 90):
            self.grade='Grade A'
        elif (self.avg >= 80):
            self.grade = 'Grade B'
        elif (self.avg >= 70):
            grade = 'Grade C'
        elif (self.avg >= 60):
            grade = 'Grade D'
        elif (self.avg >= 50):
            self.grade = 'Grade E'
        else:
            self.grade = 'Fail'

    def get(self):
        print('Name:',self.name,' Rollno:',self.roll,' Total:',self.total,' Avg:',self.avg,' Grade:',self.grade)

def main():
    s=student()
    s.set()
    s.computeavg()
    s.computegrade()
    s.get()

if __name__ == '__main__':
    main()

