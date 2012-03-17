#!/usr/bin/env python
from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)
app.config.from_pyfile('/etc/potsandpans/main.cfg')

@app.route('/sms', methods=['GET', 'POST'])
def sms():
	return 'hello world'
