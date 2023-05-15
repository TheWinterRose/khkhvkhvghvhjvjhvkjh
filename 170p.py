from tkinter import*
root=Tk()
root.title("History of space")
root.geometry("600x600")
class HIS():
    def year_2008(self,ELA,MATH):
        self.ELA=ELA
        self.MATH=MATH
    def p(self):
        total_marks=self.ELA+self.MATH
        total_marks_100=total_marks*100
        self.ELA=100
        self.MATH=100
        self.ELA+self.MATH/200

class HIM():
    def year_2008(self,ELA,MATH,SS):
        self.ELA=ELA
        self.MATH=MATH
        self.SS=SS
    def p(self):
        total_marks=self.ELA+self.MATH+self.SS
        total_marks_100=total_marks*100
        self.ELA=100
        self.MATH=100
        self.SS=100
        self.ELA+self.MATH+self.SS/300
class HISP():
    def year_2008(self,ELA,MATH,SS,S):
        self.ELA=ELA
        self.MATH=MATH
        self.SS=SS
        self.S=S
    def p(self):
        total_marks=self.ELA+self.MATH+self.SS+self.S
        total_marks_100=total_marks*100
        self.ELA=100
        self.MATH=100
        self.SS=100
        self.S=100
        self.ELA+self.MATH+self.SS/400
ohis=HIS(50,60)
ohim=HIM(60,70)
ohisp=HISP(90,90)
b=Button(root,text="Grade 3",command=ohis.p)
b.pack()
l=Label(root)
l.pack()
b2=Button(root,text="Grade 4",command=ohim.p)
b2.pack()
l2=Label(root)
l2.pack()
b3=Button(root,text="Grade 5",command=ohisp.p)
b3.pack()
l3=Label(root)
l3.pack()
root.mainloop()