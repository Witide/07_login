from flask import Flask, render_template, request, session

login_app = Flask(__name__)

@login_app.route('/')
def root():
    return render_template('form.html')

@login_app.route('/login', methods=['POST'])
def login():
    error = ""
    if not 'username' in request.form:
        error += "username"
        if not 'password' in request.form:
            error += "and password"
    elif not 'password' in request.form:
        error = "password"  
    if not error.equals(""):
        return render_template('error.html', Error = error)




    username = "not logged in as any user"
    if 'username' in request.form:
        print request.form['username']
        username = 'logged in as ' + request.form['username']
    return render_template('welcome.html', user_name = username)

@login_app.route('/logout')
def logout():
    return render_template()

if __name__ == "__main__":
    login_app.debug = True
    login_app.run()
