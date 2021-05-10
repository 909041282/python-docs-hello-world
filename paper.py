import os
import re
import copy


class Question:

    def __init__(self, num):
        self.number = num

    def setQuestion(self, content):
        data = content.split('\n')
        if len(data) != 5:
            raise ValueError('题目格式出错：' + content)
        self.title = data[0]
        self.answers = {
            'A': data[1][2:],
            'B': data[2][2:],
            'C': data[3][2:],
            'D': data[4][2:],
        }

    def setAnswer(self, answer):
        self.ture_answers = answer

    def getQuestionAndAnswer(self):
        result = copy.deepcopy(self.answers)
        result['title']=self.title
        result['answer'] = self.ture_answers
        return result


class Paper:

    def __init__(self, num, title):
        self.num = num
        self.title = title
        self.questions = {'单选':{},'多选':{}}

    def getQuestion(self, type, num):
        if type not in self.questions and num not in self.questions[type]:
            raise ValueError(f'题型{type}，')
        return self.questions[type][num].getQuestionAndAnswer()

    def getQuestionNum(self):
        return {'单选': list(self.questions['单选'].keys()),
                '多选': list(self.questions['多选'].keys())}

    def setQuestions(self, content):
        content = content.split('\n\n')
        single_part = re.split(r'\n(\d+)\.', content[0])[1:]
        for i in range(0, len(single_part), 2):
            number = int(single_part[i])
            self.questions['单选'][number] = Question(number)
            self.questions['单选'][number].setQuestion(single_part[i + 1])

        mutil_part = re.split(r'\n(\d+)\.', content[1])[1:]
        for i in range(0, len(mutil_part), 2):
            number = int(mutil_part[i])
            self.questions['多选'][number] = Question(number)
            self.questions['多选'][number].setQuestion(mutil_part[i + 1])

    def setAnswer(self, content):
        content = content.split('\n\n')
        single_part = re.split(r'\n(\d+)\.', content[0])[1:]
        for i in range(0, len(single_part), 2):
            number = int(single_part[i])
            answer = single_part[i + 1].split('\n')[1].split('|')
            answer = [i[0] for i in answer]
            self.questions['单选'][number].setAnswer(answer)

        mutil_part = re.split(r'\n(\d+)\.', content[1])[1:]
        for i in range(0, len(mutil_part), 2):
            number = int(mutil_part[i])
            answer = mutil_part[i + 1].split('\n')[1].split('|')
            answer = [i[0] for i in answer]
            self.questions['多选'][number].setAnswer(answer)


class Papers:

    def __init__(self, dir):
        self.dir = dir
        self.questions_path = os.path.join(dir, '题目.txt')
        self.answer_path = os.path.join(dir, '答案.txt')
        self.papers = {}
        self.parserQuestion()
        self.parserAnswer()

    def getQuestion(self, paper_name, type, num):
        if paper_name not in self.papers:
            raise ValueError(f'试卷 {paper_name} 不存在')
        return self.papers[paper_name].getQuestion(type, num)

    def getPaperName(self):
        return sorted(list(self.papers.keys()))

    def getQuestionTitle(self, paper_name):
        return self.papers[paper_name].title

    def getQuestionNum(self, paper_name):
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
