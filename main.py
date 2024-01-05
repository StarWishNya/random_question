import Initialize
import random
import tkinter as tk
import tkinter.filedialog
import tkinter.font

window=tk.Tk()
defautl_font=tkinter.font.nametofont("TkDefaultFont")
defautl_font.configure(family="Microsoft Yahei",size=12)
window.title("Test")
lenth=512
width=640
left=(window.winfo_screenwidth()-lenth)/2
top=(window.winfo_screenheight()-width)/2
window.geometry("%dx%d+%d+%d"%(lenth,width,left,top))
window.resizable(False,False)

show=tk.Label(window,text="Please input the filename:")
#show.place(x=0,y=0)
sign=tk.Label(window,text="None")
#sign.place(x=450,y=0)
def panduan(key,inputs):
    if '正确' in key:
        if '正确' in inputs:
            return True
        else:
            return False
    elif '错误' in key:
        if '错误' in inputs:
            return True
        else:
            return False
    else:
        if key==inputs:
            return True
        else:
            return False

def randomtest(questionlist):
    question=random.choice(questionlist)
    ques_show=tk.Label(window,text=question.stem)
    ques_show.place(x=0,y=0)

def main():
    filename=input("Please input the filename:")
    questionlist = Initialize.initialize(filename)
    model=input("Please choose a model: 1.random 2.sequence\n")
    if model=="1":
        randomtest(questionlist)
    elif model=="2":
        test(questionlist)
main()
'''def test(questionlist):
    for question in questionlist:
        print(question.stem)
        print(question.options)
        u_answer=input()
        judge=False
        while(judge==False):
            u_answer=u_answer.upper()
            if u_answer=="EXIT":
                return
            elif u_answer==question.answer:
                print("Correct!")
                judge=True
            elif u_answer=="NEXT":
                break
            elif u_answer=="SHOW":
                print(question.answer)
                print()
                break
            else:
                print("Wrong!")
                u_answer=input()
    print("Congratulations! You have finished all the questions!")
def randomtest(questionlist):
    while(1):
        question=random.choice(questionlist)
        print(question.stem)
        print(question.options)
        u_answer=input()
        judge=False
        while(judge==False):
            u_answer=u_answer.upper()
            if u_answer=="EXIT":
                return
            elif u_answer==question.answer:
                print("Correct!")
                judge=True
            elif u_answer=="NEXT":
                break
            elif u_answer=="SHOW":
                print(question.answer)
                print()
                break
            else:
                print("Wrong!")
                u_answer=input()'''	