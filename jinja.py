from flask import Flask,render_template,request,redirect,url_for

app=Flask(__name__)

@app.route("/")
def welcome():
    return "<html><H1>Welcome to the flask course</H1></html>"

@app.route("/index",methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route("/success/<int:score>")
def success(score):
    return "the marks u obtained is"+str(score)

@app.route("/successl/<int:score>")
def successl(score):
    res=""
    if score>=60:
        res="passed"
    else:
        res="failed"
    return render_template("result.html",results=res)


@app.route("/successlb/<int:score>")
def successlb(score):
    res = ""
    if score>=50:
        res="passed"
    else:
        res="failed"

    exp = {"score":score,"res":res}

    return render_template("result1.html",results=exp)

if __name__=="__main__":
    app.run(debug=True)