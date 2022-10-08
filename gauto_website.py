from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/grind')
def grindpage():
    return render_template('grindpage.html')

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == "__main__":
    app.run(debug=True)