from flask import Flask, Request, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("task-update.html")

@app.route('/task/update', methods=['GET', 'POST','PUT' ])
def TaskUpdate():

    if request.method == 'PUT':
        id = request.form['id']
        name = request.form['name']
        realized = request.form['realized']

        response = requests.post('https://todolist-api.edsonmelo.com.br/api/task/update/', json={'name': name, 'realized':realized,'id':id})

        if response.status_code == 200:
            return redirect(url_for('TaskUpdate', success=True))
        else:
            return render_template('error.html')

    success = request.args.get('success')
    error = request.args.get('error')
    return render_template("task-update.html", success=success, error=error)

@app.route('/success')
def success():
    return render_template("success.html")


if __name__ == '__main__':
    app.run()