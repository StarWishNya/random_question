import os
import re

global Questions
Questions=[]

def openfile(filename='1.txt'):
    try:
        with open(os.path.dirname(__file__) +'\\resources\\'+filename,'r',encoding='utf-8') as f:
            file=f.read()
    except Exception as e:
        print(e)
    return file

class Question:
    def __init__(self,stem,options,answer):
        self.stem=stem
        self.options=options
        self.answer=answer

def classify(file):
    global Questions
    n=int(1)
    s_question=file.split('题干:')
    for  single_question in s_question:
        stem = r'(.*?)\n'
        match = re.search(stem, single_question, re.DOTALL)
        if match:
            stem = match.group(1).strip()
        else:
            stem = None
            
        options = r'选项:(.*?)答案:'
        match = re.search(options, single_question, re.DOTALL)
        if match:
            options = match.group(1).strip()
        else:
            options = None
            
        answer = r'答案:(.*?)\n'
        match = re.search(answer, single_question, re.DOTALL)
        if match:
            answer = match.group(1).strip()
        else:
            answer = None
        if stem==None or options==None or answer==None:
            pass
        else:
            Questions.append(Question(stem, options, answer))
            #print(Questions[-1].stem, Questions[-1].options, Questions[-1].answer)
            n += 1
    return Questions

def flag():
    print('flag')
def print_question():
    print('print_question')
    for i in Questions:
        print(i.stem)
        print(i.options)
        print(i.answer)
        print()
def initialize(filename='1.txt'):
    file=openfile(filename)
    classify(file)