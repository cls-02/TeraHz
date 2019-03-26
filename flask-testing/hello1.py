from flask import Flask
app = Flask(__name__)

@app.route('/<txt>')
def root(txt):
  return 'txt={}'.format(txt)
