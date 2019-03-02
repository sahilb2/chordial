from flask import Flask, redirect
from spotify import app_Auth, user_Auth, Profile_Data
app = Flask(__name__)


@app.route('/')
def hello_world():
    print('hello world')
    auth_url = app_Auth()
    print(auth_url)
    return redirect(auth_url)


@app.route("/callback/q")
def callback():
    print("hello")
    auth_header = user_Auth()
    profile_data = Profile_Data(auth_header)
    print(profile_data)
    return str(profile_data)


if __name__ == '__main__':
    app.run()
