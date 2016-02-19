from flask import Flask
from flask import request
from flask import jsonify
from rpn import rpn 


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
			result = rpn(*rpninput)
		except ValueError:
			result = 'ValueError - Bad Input - Better Error Reporting In v2!!'

		return jsonify(answer=result)


if __name__ == "__main__":
    #app.run()
    app.run(host='0.0.0.0')
