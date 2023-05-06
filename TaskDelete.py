from flask import Flask, Request, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("task-delete.html")

@app.route('/task/delete', methods=[ 'DELETE'])
def TaskDelete():

    if request.method == 'DELETE':
        id = request.form['id']
        

        response = requests.delete('https://todolist-api.edsonmelo.com.br/api/task/delete/', json={'id': id})

        if response.status_code == 200:
            return redirect(url_for('TaskDelete', success=True))
        else:
            return render_template('error.html')

    success = request.args.get('success')
    error = request.args.get('error')
    return render_template("task-delete.html", success=success, error=error)

@app.route('/success')
def success():
    return render_template("success.html")


if __name__ == '__main__':
    app.run()