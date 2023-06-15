#program X - students grade computation using files
scores = open("scores.txt",'r')
linecount = 1
stu = []
real = []
for line in scores:
    if linecount % 2 == 0:
        tent = line.split(",")
        stu.append(name.strip('\n'))
        stu.append(tent[0])
        stu.append(tent[1])
        stu.append(tent[2].strip('\n'))
        real.append(stu)
    else:
        name = line

    linecount += 1
    stu = []
    tent = ""



for student in real:
    total = int(student[1]) + int(student[2]) + int(student[3])
    print("Name: ",student[0]," Total: ",total," Average: ",total / 3)
