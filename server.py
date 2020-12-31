from flask import Flask, request
import json
import pickle

app = Flask(__name__)

@app.route('/')
def index():
	return 'Hello World'

@app.route('/', methods=['POST'])
def hook():
#	f = open('payload.pickle','bw')
#	pickle.dump(request.form, f)
#	f.close()
	payload = json.loads(request.form['payload'])
	print(payload['repository']['name'])
	return '{"status":"success"}'

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=3000)

