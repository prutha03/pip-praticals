class students:
    def __init__(self,rollno,name):
        self.rollno=rollno
        self.name=name
class exam(students):
    def __init__(self, rollno, name):
        students.__init__(self,rollno,name)

    def marks(self):
        mylist=[]
        mysum=0
        m=0

        print("\nEnter marks of 6 subjects : ")
        for i in range (0,6):
            ele=int(input())
            mylist.append(ele)
        for m in range (len(mylist)):
            mysum=mysum+mylist[m]
        return mysum
class result(exam):

    def __init__(self, rollno, name):
        students.__init__(self,rollno,name)

    def totalmarks(self):
        total_marks=self.marks()/6
        self.total_marks = total_marks

    def display(self):
        print("\nRollno is ",self.rollno,"\nName is ",self.name,"\nMarks obtained ",self.total_marks,"\n")

r1 = result(50,"makadia prutha")
r1.totalmarks()
r1.display()
