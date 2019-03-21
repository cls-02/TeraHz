from flask import Flask
app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    value = request.json['key']
    return value

if __name__ == '__main__':
    app.run


test = open("JsonJs", "r")
req = requests.post('C:/Users/Janez%20Dolzan/Documents/Python%20projects/Spektrometer/GitHub/TeraHz/frontend/website.html')
