from flask import Flask
import google.generativeai as palm  
palm.configure(api_key ='AIzaSyD3oQq1ySn2cm330ttUhXVZNWVQ6ZFRScQ')
model = {"model": "models/chat-bison-001"}
from flask import render_template,request
app = Flask(__name__)

@app.route("/",methods=["GET", "POST"])
def index():
    return(render_template("index.html"))

@app.route("/main", methods=["GET", "POST"])
def result():
    name = request.form.get("name")
    return(render_template("main.html", result=name))

@app.route("/palm", methods=["GET", "POST"])
def palm_request():
    return(render_template("palm_request.html"))


@app.route("/palm_reply", methods=["GET", "POST"])
def palm_reply():
    q = request.form.get("q")
    #engine insert#
    r = palm.chat(
    **model,
    messages = q)
    return(render_template("palm_reply.html", result=r.last))


if __name__=="__main__":
    app.run()


