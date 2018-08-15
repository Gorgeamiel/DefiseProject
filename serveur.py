#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, request,make_response,render_template,redirect,url_for,flash,send_file,session

from hashlib import sha256
from base64 import b64encode ,b64decode

app = Flask(__name__)

@app.route('/')
def accueil():
    return render_template('Bienvenue.html')


if __name__ == '__main__':
    app.secret_key = 'Proteinismyblunt137R5Y143eaca$p^^m:ùoi'
    app.run(debug=True)
