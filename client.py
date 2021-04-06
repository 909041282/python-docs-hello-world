import json
import requests

if __name__=="__main__":

    url='http://127.0.0.1:5000/get_question'
    data={

        'paper_name':'01',
        'type':'single',
        "num":1
    }
    ret = requests.get(url,data=json.dumps(data))
    print(ret.text)
    print(json.loads(ret.text))