from flask import Flask, Request, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("new-task.html")

@app.route('/task/new', methods=['GET', 'POST'])
def NewTask():

    if request.method == 'POST':
        name = request.form['name']
        

        response = requests.post('https://todolist-api.edsonmelo.com.br/api/task/new/', json={'name': name})

        if response.status_code == 200:
            return redirect(url_for('NewTask', success=True))
        else:
            return render_template('error.html')

    success = request.args.get('success')
    error = request.args.get('error')
    return render_template("new-task.html", success=success, error=error)

@app.route('/success')
def success():
    return render_template("success.html")


if __name__ == '__main__':
    app.run()