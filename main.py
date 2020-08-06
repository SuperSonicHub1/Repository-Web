from flask import Flask, render_template, request, url_for, redirect
from display import get_repos

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', props={})


@app.route('/users/<user>/')
@app.route('/profile/<user>/')
def profile(user):
    return render_template('profile.html', props=get_repos(user))


@app.route('/lookup')
def lookup():
    return redirect(url_for('profile', user=request.args.get("lookup")))


app.run('0.0.0.0', 8080)