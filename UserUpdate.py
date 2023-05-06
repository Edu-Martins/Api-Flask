from flask import Flask, Request, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("user-update.html")

@app.route('/user/<string:username>/update', methods=['GET', 'POST','PUT'])
def Update(username):

    if request.method == 'PUT':
        name = request.form['name']
        email = request.form['email']
        response = requests.put(f'https://todolist-api.edsonmelo.com.br/api/user/{username}/update', json={'name': name, 'email': email})

        if response.status_code == 200:
            data = response.json()
            if 'error' in data or 'message' in data:
                return redirect(url_for('Update', username=username, error=True))
            else:
                return redirect(url_for('Update', username=username, success=True))
        else:
            return render_template('error.html', message='Failed to connect to API.')


    success = request.args.get('success')
    error = request.args.get('error')
    return render_template("user-update.html", success=success, error=error, username=username)

@app.route('/success')
def success():
    return render_template("success.html")


if __name__ == '__main__':
    app.run()
