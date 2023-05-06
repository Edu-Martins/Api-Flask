from flask import Flask, Request, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("task-edit.html")

@app.route('/task/edit', methods=['GET', 'POST'])
def TaskEdit():

    if request.method == 'POST':
        id = request.form['id']
        

        response = requests.post('https://todolist-api.edsonmelo.com.br/api/task/edit/', json={'id': id})

        if response.status_code == 200:
            return redirect(url_for('TaskEdit', success=True))
        else:
            return render_template('error.html')

    success = request.args.get('success')
    error = request.args.get('error')
    return render_template("task-edit.html", success=success, error=error)

@app.route('/success')
def success():
    return render_template("success.html")


if __name__ == '__main__':
    app.run()