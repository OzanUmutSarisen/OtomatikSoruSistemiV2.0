import flask
from flask import Flask
import MongoDB_Dowload
import MongoDB_Answer

app = Flask(__name__)
data = MongoDB_Dowload.DowloadStopTimer()
Question = MongoDB_Dowload.DowloadQuestions()

logined = False
number = "2018555055"

@app.route("/")
def login():
    global logined
    logined = False
    return flask.render_template("login.html")

@app.route("/selectvideo", methods=['POST'])
def selectVideo():
     global logined
     global number
     if logined == False:
         number = flask.request.form["number"]
         logined = True
         return flask.render_template("videoSelect.html", number=number)
     else:
         return flask.render_template("videoSelect.html", number=number)


@app.route("/videoPlay", methods=["POST"])
def videoPlay():
    return flask.render_template("Index.html", data=data, Question=Question, QuestionSize=len(Question))


@app.route("/takeData", methods=['POST'])
def takeData():
    global number
    answer = flask.request.form["answers"]
    question = flask.request.form["question"]
    MongoDB_Answer.Upload(answer=answer, question=question, studentNumber=number)
    return "hello"

@app.route("/videoEnd", methods=['POST'])
def videoEnd():
    return "hello"



if __name__ == '__main__':
    app.run()