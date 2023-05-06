from flask import Flask,  render_template, request, redirect, url_for
import requests


app = Flask(__name__)

@app.route('/')
def homeLogin():
    return render_template("user-login.html")

@app.route('/user/login', methods=['GET', 'POST'])
def UserLogin():

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        response = requests.post('https://todolist-api.edsonmelo.com.br/api/user/login/', json={'username': username,'password': password})

        if response.status_code == 200:
            data = response.json()
            if 'error' in data or 'message' in data:
                return redirect(url_for('UserLogin', error=True))
            else:
               return redirect(url_for('UserLogin', success=True))
        else:
            return render_template('error.html', message='Failed to connect to API.')
        
    success = request.args.get('success')
    error = request.args.get('error')
    return render_template("user-login.html", success=success, error=error)



@app.route('/success')
def success():
    return render_template("success.html")

if __name__ == '__main__':
    app.run()