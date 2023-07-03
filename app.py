from flask import Flask, render_template
import requests, json

app = Flask(__name__)
url = 'http://127.0.0.1:8000/api/'
c = 0

@app.route('/')
def index():  # put application's code here
    global c
    if c == 0:
        c = requests.get(url + 'leaderboardforce').json()
    else:
        d = requests.get(url + 'leaderboard').json()
        if d['status'] == 'changed':
            c = d
    return render_template("leaderboard.html", meiste_kilometer=c['meiste_kilometer'], kilometer=c['kilometer'], klassen=c['klassen'])

if __name__ == '__main__':
    app.run()
