import os
from flask import Flask, url_for, render_template, request, redirect, session

app = Flask(__name__)

# In order to use "sessions", you need a "secret key".
# This is something random you generate.
# For more info see: https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY

app.secret_key = os.environ.get('SECRET_KEY')

x = 0

def count1():
    count1 = x
    if session['password_choice'] == "password3":
        count1 += 1
    return count1
    
def count2():
    count1 = x
    if session['password_choice'] == "answer5":
        count1 += 1
    return count2
    
def count3():
    count1 = x
    if session['password_choice'] == "p3_1":
        count1 += 1
    return count3

@app.route('/')
def renderMain():
    return render_template('home.html')

@app.route('/startOver')
def startOver():
    session.clear() #clears variable values and creates a new session
    return redirect(url_for('renderMain')) # url_for('renderMain') could be replaced with '/'

@app.route('/page1', methods=['POST', 'GET'])
def renderPage1():
    if request.method == 'POST':
        password_choice = request.form['password']
        session['password_choice'] = password_choice
        return render_template('dyk1.html')
    
    return render_template('page1.html')

@app.route('/page2', methods=['POST', 'GET'])
def renderPage2():
    if request.method == 'POST':
        answer_choice = request.form['answer']
        session['answer_choice'] = answer_choice
        return render_template('dyk2.html')
    return render_template('page2.html')

@app.route('/page3', methods=['POST', 'GET'])
def renderPage3():
    if request.method == 'POST':
        p3_choice = request.form['anw']
        session['p3_choice'] = p3_choice
        return render_template('dyk3.html')
    return render_template('page3.html')  

@app.route('/qscore', methods=['POST', 'GET'])
def renderScore():
    score = count1()
    return render_template('qscore.html', score=score)  
   
    
if __name__ == "__main__":
    app.run(debug=False)
