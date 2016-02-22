from flask import Flask
from flask import request
from flask import jsonify
import rpncontroller
import shunt

app = Flask(__name__)

@app.route("/")
def hello():
    return jsonify(info = "RPN API")

@app.route("/v1/rpn", methods=["POST"])
def v1rpnweb():

	json = request.json

	if request.json:
		rpninput = request.json.get('input')

		try: 
			result = rpncontroller.dorpnalt(rpninput)
			resp = jsonify(answer=result)
		except IndexError:
			resp = jsonify(error=rpncontroller.INDEX_ERROR)
			resp.status_code = 400
		except ValueError:
			resp = jsonify(error=rpncontroller.VALUE_ERROR)
			resp.status_code = 400
		
		return resp

@app.route("/v1/calculator", methods=["POST"])
def v1calculator():

	json = request.json

	if request.json:
		cinput = request.json.get('input')

		c = shunt.Calculator()

		try:
			result = c.calculate(cinput)
			resp = jsonify(answer=result)
		except Exception as e:
			resp = jsonify(error='%s' % e)
			resp.status_code = 400
		
		return resp


if __name__ == "__main__":
    #app.run()
    app.debug = True
    app.run(host='0.0.0.0')

