import os
import json
import pickle
import random
from flask import Flask, render_template, request, redirect, url_for, Response
from hotel_sentiment_analysis import return_reviews


app = Flask(__name__)
hotel_data_path = 'static/data/hotel_data'

@app.route('/', methods=['GET', 'POST'])
def index():
	# Get hotel lists 
	all_dirs = os.listdir(hotel_data_path)
	if request.method == 'POST':
		hotel_name = request.form.get('hotel_name')
		hotel_path = os.path.join('static/data/hotel_data', hotel_name)
		pickle_path = os.path.join(hotel_path, 'meta.pkl')
		with open(pickle_path, 'rb') as file:
			meta = pickle.load(file)
		#hotel_score = random.uniform(2.5, 5)
		hotel_score = return_reviews(hotel_name)[-1] # calculated star based on sentiment analysis

		image_paths = [os.path.join('static/data/', x['image']) for x in meta['images']]
		
		if len(meta['rooms']) > 0:
			hotel_price = meta['rooms'][0]['price']
		else:
			hotel_price = 100

		return render_template('hotel_page.html', hotel_name=hotel_name,
								image_paths=image_paths, description=meta['description'],
								hotel_score=round(hotel_score, 1),
								main_features=meta['main_amenities'],
								whats_around=meta['whats_around'],
								positive_reviews=return_reviews(hotel_name)[0],
								negative_reviews=return_reviews(hotel_name)[1],
								neutral_reviews=return_reviews(hotel_name)[2],
								hotel_price=hotel_price)

	return render_template('index.html', all_hotel_names=json.dumps(all_dirs))

@app.route('/about')
def about():
	return render_template('about.html')

if __name__ == '__main__':
  app.run(port=33507)
