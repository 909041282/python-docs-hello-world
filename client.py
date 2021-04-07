import json
import requests

url = 'http://127.0.0.1:5000/'

def getUrl(data):
    ret = requests.get(url+'get_question',data=json.dumps(data))
    print(json.loads(ret.text))

def getQuestion():
    data={
        'function':'question',
        'paper_name':'01',
        'type':'single',
        "num":1
    }
    getUrl(data)

def getAllPapers():
    data={
        'function': 'allPaper',
    }
    getUrl(data)

def getPaper():
    data={
        'function': 'paper',
        'paper_name':'01'
    }
    getUrl(data)

if __name__=="__main__":
    getQuestion()
    getAllPapers()
    getPaper()
