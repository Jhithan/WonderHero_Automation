from pyautogui import prompt, password
from flask import render_template 
usernames = []
passwords = []
def get_username():
    username = prompt(text='', title='Enter your username', default=None)
    if username:
        usernames.append(username)
    return render_template('grindpage.html')

def get_password():
    password = password(text='', title='Enter your password', default=None, mask='*')
    if password:
        passwords.append(password)
