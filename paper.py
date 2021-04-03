import os
import re
class Question:

    def __init__(self,num):
        self.number = num

    def setQuestion(self,content):
        data=content.split('\n')
        if len(data) !=5:
            raise ValueError('题目格式出错：'+content)
        self.title=data[0]
        self.answers={
            'A':data[1][2:],
            'B':data[2][2:],
            'C':data[3][2:],
            'D':data[4][2:],
        }

    def setAnswer(self,answer):
        self.ture_answers=answer

class Paper:

    def __init__(self,num,title):
        self.num = num
        self.title=title
        self.single={}
        self.mutil={}

    def setQuestions(self,content):
        content = content.split('\n\n')
        single_part = re.split(r'\n(\d+)\.',content[0])[1:]
        for i in range(0,len(single_part),2):
            number=single_part[i]
            self.single[number]=Question(number)
            self.single[number].setQuestion(single_part[i+1])

        mutil_part = re.split(r'\n(\d+)\.',content[1])[1:]
        for i in range(0,len(mutil_part),2):
            number=mutil_part[i]
            self.mutil[number]=Question(number)
            self.mutil[number].setQuestion(mutil_part[i + 1])

    def setAnswer(self,content):
        content = content.split('\n\n')
        single_part = re.split(r'\n(\d+)\.',content[0])[1:]
        for i in range(0,len(single_part),2):
            number=single_part[i]
            answer = single_part[i+1].split('\n')[1].split('|')
            answer = [i[0] for i in answer]
            self.single[number].setAnswer(answer)

        mutil_part = re.split(r'\n(\d+)\.',content[1])[1:]
        for i in range(0,len(mutil_part),2):
            number = mutil_part[i]
            answer = mutil_part[i+1].split('\n')[1].split('|')
            answer = [i[0] for i in answer]
            self.mutil[number].setAnswer(answer)


class Papers:

    def __init__(self,dir):
        self.dir=dir
        self.questions_path=os.path.join(dir,'题目.txt')
        self.answer_path=os.path.join(dir,'答案.txt')
        self.papers={}
        self.parserQuestion()
        self.parserAnswer()

    def parserQuestion(self):
        data=open(self.questions_path,'r',encoding='utf8').read()
        papers = re.split(r'JC(\d+)\s*(.*)\n',data)[1:]
        for i in range(0,len(papers),3):
            self.papers[papers[i]] = Paper(papers[i],papers[i+1])
            self.papers[papers[i]].setQuestions(papers[i + 2])
        pass

    def parserAnswer(self):
        data = open(self.answer_path, 'r',encoding='utf8').read()
        papers = re.split(r'JC(\d+)(.*)\n',data)[1:]
        for i in range(0,len(papers),3):
            self.papers[papers[i]].setAnswer(papers[i+2])
        pass

Papers('data/心理咨询师/')