# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets, QtCore
from ui.main import Ui_MainWindow
from paper import Papers
import os, sys


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.current_question_num = 1
        self.question = None
        self.cbb_file.addItems(os.listdir('./data'))
        self.cbb_question_type.addItems(['单选', '多选'])

    def load_papers(self, name):
        if name:
            self.papers = Papers('./data/' + name)
            self.cbb_papers.addItems(self.papers.getPaperName())

    def onFilesChanged(self, name):
        self.load_papers(name)

    def onPapersChanged(self, name):
        self.getQuestion()

    def setQuestion(self, question):
        self.cb_A.setChecked(False)
        self.cb_B.setChecked(False)
        self.cb_C.setChecked(False)
        self.cb_D.setChecked(False)
        self.lb_answer.setText('')
        self.lb_title.setText(question['title'])
        self.cb_A.setText(question['A'])
        self.cb_B.setText(question['B'])
        self.cb_C.setText(question['C'])
        self.cb_D.setText(question['D'])

    def onQuestionTypeChanged(self, name):
        self.getQuestion()

    def getQuestionNum(self):
        nums = self.papers.getQuestionNum(self.cbb_papers.currentText())
        return len(nums[self.cbb_question_type.currentText()])

    def getQuestion(self):
        if self.cbb_papers.currentText() in self.papers.getPaperName() and self.cbb_question_type.currentText():
            self.question = self.papers.getQuestion(self.cbb_papers.currentText(), self.cbb_question_type.currentText(),
                                                    self.current_question_num)
            self.setQuestion(self.question)

    def checkAnswer(self):
        answer = []
        if self.cb_A.isChecked():
            answer.append('A')
        if self.cb_B.isChecked():
            answer.append('B')
        if self.cb_C.isChecked():
            answer.append('C')
        if self.cb_D.isChecked():
            answer.append('D')
        return answer

    def onPreviousClicked(self):
        self.current_question_num -= 1
        if self.current_question_num < 1:
            self.current_question_num = self.getQuestionNum()
        self.getQuestion()

    def onSureClicked(self):
        if set(self.checkAnswer()) == set(self.question['answer']):
            self.lb_answer.setText('回答正确')
        else:
            self.lb_answer.setText('回答错误，正确答案是：' + ''.join(self.question['answer']))

    def onNextClicked(self):
        self.current_question_num += 1
        if self.current_question_num > self.getQuestionNum():
            self.current_question_num = 1
        self.getQuestion()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
