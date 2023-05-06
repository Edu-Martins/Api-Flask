from flask import Flask, Request, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("user-new.html")

@app.route('/user/new', methods=['GET', 'POST'])
def UserNew():

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']

        response = requests.post('https://todolist-api.edsonmelo.com.br/api/user/new/', json={'name': name, 'email': email , 'username': username, 'password': password})

        if response.status_code == 200:
            return redirect(url_for('UserNew', success=True))
        else:
            return render_template('error.html')

    success = request.args.get('success')
    error = request.args.get('error')
    return render_template("user-new.html", success=success, error=error)

@app.route('/success')
def success():
    return render_template("success.html")


if __name__ == '__main__':
    app.run()