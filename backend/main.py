from flask import Flask, redirect, url_for, request
app = Flask(__Name__)

@app.route('/list')
def list():
   #Return list json

@app.route('/load'):
def load():
   #Request args, load json

@app.route('/deposit'):
def deposit():
   #Request .json, store json
   if request.isJson():
      request.json.
