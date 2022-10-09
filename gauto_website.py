from flask import Flask, render_template, request
import WonderHero_Automation

app = Flask(__name__, template_folder='templates')

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/grind', methods=['GET', 'POST'])
def grindpage():
    if request.method == 'POST':
        if request.form.get('grind') == 'Grind':
            return WonderHero_Automation.get_username()
    elif request.method == 'GET':
        return render_template('grindpage.html')

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == "__main__":
    app.run(debug=True)