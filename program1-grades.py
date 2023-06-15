'''Program 1 - Consider the marks of 5 subjects obtained from user input.
Calculate the grade based on the criteria: >=90-A, >=80-B, >=70-C, >=60-D, >=50-E, <50-F.
Perform necessary validations on marks such as negative marks, non-numeric marks.
Finally display student name, rollno, total marks and grade.'''

name = input('Enter name ')
roll = input('Enter roll no ')
print('Enter Marks ')
s1=int(input('java '))
s2=int(input('C '))
s3=int(input('c++ '))
s4=int(input('dbms '))
s5=int(input('os '))

if (s1 < 0 or s2 < 0 or s3 < 0 or s4 < 0 or s5 < 0):
    print('Cant perform operation')
    quit()
tot=s1 + s2 + s3 + s4 + s5
avg=tot / 5
print('Student name: ',name, end=' ')
print('Roll no: ',roll, end=' ')
print('Total marks: ',tot,end=' ')
if (s1 < 50 or s2 < 50 or s3 < 50 or s4 < 50 or s5 < 50):
    print('Grade F')
    quit()
if(avg >= 90):
    print('Grade A')
elif(avg >= 80 and avg < 90):
    print("Grade B")
elif(avg >= 70 and avg < 80):
    print('Grade C')
elif(avg >= 60 and avg < 70):
    print('Grade D')
elif(avg >= 50 and avg < 60):
    print('Grade E')
else:
    print('Grade F')
