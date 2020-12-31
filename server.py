from flask import Flask, request
import json
import pickle

app = Flask(__name__)

@app.route('/')
def index():
	return 'Hello World'

@app.route('/', methods=['POST'])
def hook():
	f = open('payload.pickle','w')
	pickle(f,request.form)
	f.close()
	return '{"status":"success"}'

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=3000)

