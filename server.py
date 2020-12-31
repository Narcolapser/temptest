from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/')
def index():
	return 'Hello World'

@app.route('/', methods=['POST'])
def hook():
	print(request.form)
	payload = json.loads(request.form[0][1])
	return '{"status":"success"}'

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=3000)

