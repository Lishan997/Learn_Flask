from flask import Flask, redirect, url_for

##WSGI Application
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hi Mithila Lishan!</h1>"

@app.route("/members")
def member_welcome():
    return "<h1>Hi Guys!</h1>"   

@app.route("/printage/<int:age>")
def display_age(age):
    age_category = ""
    if age >= 50:
        age_category = "Adult"
    else:
        age_category = "Young" 

    return "<h1> Your are " + age_category + "</h1>" 

@app.route("/printname/<name>")
def display_name(name):
    return "<h1>My Name is " + name + "</h1>"  

#Building URL Dinamically
@app.route('/success/<int:score>')
def success(score):
    return "The Person has passed and the mark is " + str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "The Person has failed and the mark is " + str(score)  

@app.route('/results/<int:marks>')
def result(marks):
    results = ""

    if marks < 50:
        results = 'fail'  
    else:
        results = 'success' 
    return redirect(url_for(results,score=marks))         

#Debug mode
if __name__=='__main__':
    app.run(debug=True)    