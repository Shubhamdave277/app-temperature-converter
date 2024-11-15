from flask import Flask, render_template_string, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

with open('login.html', 'r') as html_file:
    template = html_file.read()

with open('dashboard.html', 'r') as dashboard_file:
    dashboard_html = dashboard_file.read()

@app.route('/', methods=['GET', 'POST'])
def login():
    message = ""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'admin' and password == 'password':
            session['username'] = username
            return redirect(url_for('dashboard'))
        else:
            message = "Invalid username or password."
    if 'username' in session:
        return redirect(url_for('dashboard'))
    return render_template_string(template, message=message)

@app.route('/dashboard', methods=['POST'])
def dashboard(): 
    return render_template_string(dashboard_html)
    

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('/'))

if __name__ == '__main__':
    app.run(debug=True)