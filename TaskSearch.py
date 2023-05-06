from flask import Flask, Request, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("task-search.html")

@app.route('/task/search', methods=['GET', 'POST'])
def TaskSearch():

    if request.method == 'POST':
        search = request.form['search']
        

        response = requests.post('https://todolist-api.edsonmelo.com.br/api/task/search/', json={'search': search})

        if response.status_code == 200:
            return redirect(url_for('TaskSearch', success=True))
        else:
            return render_template('error.html')

    success = request.args.get('success')
    error = request.args.get('error')
    return render_template("task-search.html", success=success, error=error)

@app.route('/success')
def success():
    return render_template("success.html")


if __name__ == '__main__':
    app.run()