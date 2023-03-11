from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

app.secret_key = 'abfklfgalfa'

@app.route('/')
def index():
    if 'site_visits' not in session:
        session['site_visits'] = 1
    else:
        session['site_visits'] += 1
    if 'count' not in session:
        session['count'] = 0
        
    return render_template('index.html')

@app.route('/counter')
def counter():
    session['count'] += 1
    session['site_visits'] -= 1
    return redirect('/')

@app.route('/double_counter')
def double_counter():
    session['count'] += 2
    session['site_visits'] -= 1
    return redirect('/')

@app.route('/user_increment', methods=['POST'])
def user_increment():
    session['site_visits'] -= 1
    session['count'] += (int(request.form['increment'])-1)
    return redirect('/')

@app.route('/destroy_session')
def reset():
    session.clear()
    return redirect('/')

if __name__=='__main__':
    app.run(debug=True)

"""
>>> import base64
>>> base64.urlsafe_b64decode('eyJjb3VudCI6Nywic2l0ZV92aXNpdHMiOjR9')
b'{"count":7,"site_visits":4}'
>>>
"""