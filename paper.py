import os
import re


class Paper:

    def __init__(self, num, title):
        self.num = num
        self.title = title
        self.questions = {'单选':{},'多选':{}}

    def getQuestion(self, type, num):
        if type not in self.questions and num not in self.questions[type]:
            raise ValueError(f'题型{type}，')
        return self.questions[type][num]

    def getQuestionNum(self):
        return {'单选': list(self.questions['单选'].keys()),
                '多选': list(self.questions['多选'].keys())}

    def paserQuestion(self,data):
        data = data.split('\n')
        if len(data) != 5:
            raise ValueError('题目格式出错：' + data)
        question ={"title":data[0],
            'A': data[1][2:],
            'B': data[2][2:],
            'C': data[3][2:],
            'D': data[4][2:],
        }
        return question

    def setQuestions(self, content):
        content = content.split('\n\n')
        single_part = re.split(r'\n(\d+)\.', content[0])[1:]
        for i in range(0, len(single_part), 2):
            number = int(single_part[i])
            self.questions['单选'][number] = self.paserQuestion(single_part[i + 1])

        mutil_part = re.split(r'\n(\d+)\.', content[1])[1:]
        for i in range(0, len(mutil_part), 2):
            number = int(mutil_part[i])
            self.questions['多选'][number] = self.paserQuestion(mutil_part[i + 1])

    def setAnswer(self, content):
        content = content.split('\n\n')
        single_part = re.split(r'\n(\d+)\.', content[0])[1:]
        for i in range(0, len(single_part), 2):
            number = int(single_part[i])
            answer = single_part[i + 1].split('\n')[1].split('|')
            self.questions['单选'][number]['answer']= [i[0] for i in answer]

        mutil_part = re.split(r'\n(\d+)\.', content[1])[1:]
        for i in range(0, len(mutil_part), 2):
            number = int(mutil_part[i])
            answer = mutil_part[i + 1].split('\n')[1].split('|')
            self.questions['多选'][number]['answer']= [i[0] for i in answer]


class Papers:

    def __init__(self, dir):
        self.dir = dir
        self.questions_path = os.path.join(dir, '题目.txt')
        self.answer_path = os.path.join(dir, '答案.txt')
        self.papers = {}
        self.parserQuestion()
        self.parserAnswer()

    def getQuestion(self, paper_name, type, num):
        paper_name = paper_name.split('--')[0]
        if paper_name not in self.papers:
            raise ValueError(f'试卷 {paper_name} 不存在')
        return self.papers[paper_name].getQuestion(type, num)

    def getPaperName(self):
        return sorted([f'{i}--{self.getQuestionTitle(i)}'for i in self.papers])

    def getQuestionTitle(self, paper_name):
        paper_name=paper_name.split('--')[0]
        return self.papers[paper_name].title

    def getQuestionNum(self, paper_name):
        paper_name = paper_name.split('--')[0]
        return self.papers[paper_name].getQuestionNum()

    def parserQuestion(self):
        data = open(self.questions_path, 'r', encoding='utf8').read()
        papers = re.split(r'JC(\d+)\s*(.*)\n', data)[1:]
        for i in range(0, len(papers), 3):
            self.papers[papers[i]] = Paper(papers[i], papers[i + 1])
            self.papers[papers[i]].setQuestions(papers[i + 2])
        pass

    def parserAnswer(self):
        data = open(self.answer_path, 'r', encoding='utf8').read()
        papers = re.split(r'JC(\d+)(.*)\n', data)[1:]
        for i in range(0, len(papers), 3):
            self.papers[papers[i]].setAnswer(papers[i + 2])
        pass
