from app import app
from flask import g, session, flash
from flask import redirect, render_template, url_for

#Index view
@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    return 'Index'