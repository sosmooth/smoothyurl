from app import app
from flask import g, render_template, redirect, url_for, session, flash


#Index view
@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    return 'Index'