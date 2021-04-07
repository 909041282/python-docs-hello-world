from flask import Flask,abort,request
from paper import Papers
import json
app = Flask(__name__)

papers = Papers('data/心理咨询师/')


@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/index")
def index():
    return "Hello, index!"


@app.route("/get_question",methods=['GET','POST'])
def getQuestion():
    try:
        data=json.loads(request.data)
        if data['function']=='allPaper':
            result = papers.getAllPaper()
        elif data['function']=='paper':
            result = papers.getAllQuestion(data['paper_name'])
        elif data['function']=='question':
            result = papers.getQuestion(data['paper_name'],data['type'],data['num'])
        return json.dumps(result)
    except:
        abort(500)



app.run("0.0.0.0",5000)