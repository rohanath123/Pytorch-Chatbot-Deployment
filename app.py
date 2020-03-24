from flask import Flask, render_template, request
from forms import *
import torch
import numpy as np

app = Flask(__name__)

app.config['SECRET_KEY'] = 'rohan'

def get_prediction(sentence):
	output = evaluateInput(encoder, decoder, searcher, voc, sentence)
	return output

@app.route('/', methods = ['GET', 'POST'])
def ip2():
	form = inputForm()
	output = ""
	if form.is_submitted():

		result = request.form
		result = result.get('input')

		output = get_prediction(result)
		return render_template('ip2.html', form = form, result = output)
	return render_template('ip2.html', form = form, result = output)
	
if __name__ == "__main__":
	from model import *
	encoder = torch.load('encoder2.pkl')
	decoder = torch.load('decoder2.pkl')
	encoder.eval()
	decoder.eval()
	voc = torch.load('voc2.pkl')
	searcher = GreedySearchDecoder(encoder, decoder)
	app.run(host = '0.0.0.0', port = '80')