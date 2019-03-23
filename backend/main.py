from flask import Flask, redirect, url_for, request, render_template
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
      request.get_json()



@app.route('/graph')
def graph(chartID = 'chart_ID', chart_type = 'line', chart_height = 500):
	chart = {"renderTo": chartID, "type": chart_type, "height": chart_height,}
	series = [{"name": 'Label1', "data": [1,2,3]}, {"name": 'Label2', "data": [4, 5, 6]}]
	title = {"text": 'My Title'}
	xAxis = {"categories": ['xAxis Data1', 'xAxis Data2', 'xAxis Data3']}
	yAxis = {"title": {"text": 'yAxis Label'}}
	return render_template('index.html', chartID=chartID, chart=chart, series=series, title=title, xAxis=xAxis, yAxis=yAxis)
 
if __name__ == "__main__":
	app.run(debug = True, host='0.0.0.0', port=8080, passthrough_errors=True)
