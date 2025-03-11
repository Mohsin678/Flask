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

@app.route("/successbv/<int:score>")
def successbv(score):
    return render_template("result.html",results=score)




@app.route('/fail/<int:score>')
def fail(score):
    return render_template('result.html',results=score)

@app.route("/submit",methods=["GET","POST"])
def submit():
    tot_score = 0
    if request.method=="POST":
        science = float(request.form["science"])
        maths = float(request.form["maths"])
        c= float(request.form["c"])
        data_science = float(request.form["datascience"])

        tot_score = (science+maths+c+data_science)
    else:
        return render_template("getresult.html")
    return redirect(url_for("successbv",score=tot_score))








if __name__=="__main__":
    app.run(debug=True)