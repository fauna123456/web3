from flask import Flask,render_template,request
import google.generativeai as palm
 
palm.configure(api_key="AIzaSyC38PU9OO-c0mRV0bTwSm0C9eoDr77PJas")
model = {"model":"models/chat-bison-001"}
app = Flask(__name__)
 
@app.route("/",methods=["GET","POST"])
def index():
    return(render_template("index.html"))
 
@app.route("/main",methods=["GET","POST"])
def main():
    r = request.form.get("q")
    return(render_template("main.html",r=r))
 
@app.route("/genAI",methods=["GET","POST"])
def genAI():
    q = request.form.get("q")
    r = palm.chat(**model,messages=q)
    return(render_template("genAI.html",r=r.last))
 
if __name__ == "__main__":
    app.run()
