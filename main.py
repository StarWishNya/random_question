import Initialize
import random
def test(questionlist):
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
                break
            else:
                print("Wrong!")
                u_answer=input()

def main():
    questionlist = Initialize.initialize()
    model=input("Please choose a model: 1.random 2.sequence\n")
    if model=="1":
        randomtest(questionlist)
    elif model=="2":
        test(questionlist)
main()