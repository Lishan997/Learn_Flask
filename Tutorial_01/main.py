from flask import Flask, redirect, url_for, render_template, request

#import 'request' because we need to handle posted values
##WSGI Application
app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    grade=""
    if score >= 75:
        grade = "You have grade A"
    elif score >= 65:
        grade = "You have grade B"  
    else:
        grade = "You have grade C"
    return render_template('result.html', show_result=grade)
          

@app.route('/fail/<int:score>')
def fail(score):
    return "The Person has failed and the average mark is " + str(score)  

##After click submit button it comes here 
@app.route('/submit', methods=['POST', 'GET'])   
def submit():
    total_score = 0

    if request.method =='POST':
        scince_marks = float(request.form['science'])
        maths_marks = float(request.form['maths'])
        c_marks = float(request.form['c'])
        datascince_marks = float(request.form['datascience'])
        total_marks = (scince_marks+maths_marks+c_marks+datascince_marks)/4

    result = ""    

    if total_marks >= 50:
        result = "success"
    else:
        result = "fail"    
    return redirect(url_for(result,score=total_marks))    

#Debug mode
if __name__=='__main__':
    app.run(debug=True)    

