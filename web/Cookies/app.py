from flask import Flask, request, render_template, make_response, redirect, Response
from werkzeug.security import check_password_hash, generate_password_hash
import hashlib

app = Flask(__name__)


users = {
    "administrator": generate_password_hash("s3cr3ts3cur3uncr4ck4bl3p4$$w0rd@!#(%%(*!%iewgrkjhgks45jh7ah75HKJSEH5JFHSEKJSHGKGR6iqfds"),
    "test": generate_password_hash("test"),
}


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if the username exists and the password is correct
        if username in users and check_password_hash(users[username], password):

            # Generate a hash of the username
            cookie = hashlib.sha256(username.encode()).hexdigest()

            # Create a response object that includes redirection
            resp = make_response(redirect('/home'))

            # Set the cookie on the response
            resp.set_cookie('user', cookie)

            return resp
        else:
            error = 'Invalid credentials'
            return render_template('login.html', error=error)

@app.route('/robots.txt')
def robots():
    return Response("User-agent: *\nDisallow: /administrator", mimetype="text/plain")

@app.route('/')
def index():
    user_cookie = request.cookies.get('user')
    if user_cookie == hashlib.sha256('administrator'.encode()).hexdigest() or user_cookie == hashlib.sha256('test'.encode()).hexdigest():
        return redirect('/home')
    else:
        return redirect('/login')  # Redirects to the login page

@app.route('/home')
def home():
    user_cookie = request.cookies.get('user')

    username = None
    for user, hashed_password in users.items():
        if user_cookie == hashlib.sha256(user.encode()).hexdigest():
            username = user
            break

    if username is not None:
        return render_template('home.html', username=username)
    else:
        return redirect('/login')



@app.route('/administrator')
def admin_page():
    user_cookie = request.cookies.get('user')
    if user_cookie == hashlib.sha256('administrator'.encode()).hexdigest():
        return 'pecan{1_h4x3d_t3h_c00k135}'
    else:
        return 'Only the administrator can access this page'

@app.route('/logout', methods=['POST'])
def logout():
    resp = make_response(redirect('/login'))
    resp.set_cookie('user', '', expires=0)
    return resp

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
