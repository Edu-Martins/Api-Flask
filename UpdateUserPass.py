from flask import Flask, Request, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("user-updatepass.html")

@app.route('/user/updateuserpass', methods=['GET', 'POST','PUT'])
def UpdateUserPass(username):

    if request.method == 'PUT':
        username = request.form['username']
        password = request.form['password']
        new_username = request.form['new_username']
        new_password = request.form['new_password']
        
        response = requests.put(f'https://todolist-api.edsonmelo.com.br/api/user/updateuserpass', json={'username': username, 'password':password, 'new_username':new_username,'new_password':new_password})

        if response.status_code == 200:
            data = response.json()
            if 'error' in data or 'message' in data:
                return redirect(url_for('UpdateUserPass', username=username, error=True))
            else:
                return redirect(url_for('UpdateUserPass', username=username, success=True))
        else:
            return render_template('error.html', message='Failed to connect to API.')


    success = request.args.get('success')
    error = request.args.get('error')
    return render_template("user-updatepass.html", success=success, error=error, username=username)

@app.route('/success')
def success():
    return render_template("success.html")


if __name__ == '__main__':
    app.run()
