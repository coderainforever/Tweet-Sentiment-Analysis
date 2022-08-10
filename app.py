from flask import Flask, render_template, url_for
from flask import request as req
import requests


app = Flask(__name__)


@app.route("/",methods=["GET","POST"])
def Index():
    return render_template("index.html")

@app.route("/Sentiment",methods=["GET","POST"])
def Analyze():
    if req.method=="POST":
        API_URL = "https://api-inference.huggingface.co/models/cardiffnlp/twitter-roberta-base-sentiment-latest"
        headers = {"Authorization": "Bearer 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"}

        data = req.form["data"]


        def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()
	
        output = query({
            "inputs": data,
        })

        temp = output[0]

        return render_template("index.html", negative=temp[0]['label'], negscore=temp[0]['score'], neutral=temp[1]['label'], neuscore=temp[1]['score'], positive=temp[2]['label'], poscore=temp[2]['score'])
    else:
        return render_template("index.html")

if __name__ == '__main__':
    app.debug=False # make it false during production
    app.run()
