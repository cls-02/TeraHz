from flask import Flask
application = Flask(__name__)
@application.route('/')
def helloworld():
    return 'Hello there, world!'
