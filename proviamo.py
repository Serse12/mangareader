from flask import Flask
from flask import render_template
from flask import url_for
from flask import request 
from flask import session 
from flask import flash 

import json

from markupsafe import escape
from werkzeug.utils import secure_filename


app= Flask(__name__)
app.secret_key = b'YnH($U?jWwQ(Z1xrp;iLqq?J:ATQ)a?.y?2-Ju2!}BiT4Eue7$'

#url_for('static', filename='style.css')

@app.route("/")
@app.route("/<name>")
def salutatizio(name=None):
    flash("Ciao")

    if 'username' in session:
        name = session["username"]

    if request.method == 'POST':
        return render_template('home.html',name=name)
    if request.method == 'GET':
        return render_template('home.html',name=name)
    return render_template('home.html',name=name)


@app.route("/intero")
@app.route("/intero/<int:name>")
def scriviintero(name=None):
    res={'intero' : name}
    return json.dumps(res)

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('salutatizio'))

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['the_file']
        file.save(f"/var/www/uploads/{secure_filename(file.filename)}")

@app.route("/me")
def me_api():
    user = get_current_user()
    return {
        "username": user.username,
        "theme": user.theme,
        "image": url_for("user_image", filename=user.image),
    }

@app.route("/users")
def users_api():
    users = get_all_users()
    return [user.to_json() for user in users]
