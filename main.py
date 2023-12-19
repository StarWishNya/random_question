import Initialize
import random
def test(questionlist):
    for question in questionlist:
        print(question.stem)
        print(question.options)
        print(question.answer)
        print()
def main():
    questionlist = Initialize.initialize()
    while(1):
        question=random.choice(questionlist)
        print(question.stem)
        print(question.options)
        u_answer=input()
        judge=False
        while(judge==False):
            if u_answer==question.answer:
                print("Correct!")
                judge=True
            else:
                print("Wrong!")
                u_answer=input()

main()