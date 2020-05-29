import pickle
from bs4 import BeautifulSoup
import os
import requests
import time
from PIL import Image
import urllib

# Go over the hotels and save the information
def save_hotel_info(hotel_name,
					address_template,
					check_in,
					check_out,
					root_save_folder,
					sleep_between_queries=0,
					max_images_per_hotel=5):
	try:


			# Sleep for 'sleep' seconds between queries (0.2sec)
		time.sleep(sleep_between_queries)

		# Create a meta dictionary for this hotel
		hotel_meta = {}
		hotel_meta['name'] =  hotel_name

		# Create the URL for this hotel search
		url = address_template.format(hotel_name, check_in, check_out)
		print(url)
		hotel_meta['url'] = url
		# Get the html page
		request = requests.get(url, allow_redirects=True)
		html_content = request.text



		# Parse the content
		soup = BeautifulSoup(html_content, 'html.parser')

		# Save images
		## Image ID: this ID is incremented after each image is saved
		image_id = 0
		## Find image URLS
		images_info = soup.find('div', {"class": "canvas cont-bd widget-carousel-enabled"})
		images_info = images_info.find_all('li', {"class": "image"})
		## Number of images to be saved
		n_image_to_save = min(max_images_per_hotel, len(images_info))
		## A list of {local_image_address, 'caption'}
		images = []

		# Create the output folder and savings
		save_folder_path = os.path.join(root_save_folder, hotel_name)
		if not os.path.exists(save_folder_path):
			os.makedirs(save_folder_path)

		# Save html content
		with open(os.path.join(save_folder_path, 'page.html'), 'wb') as file:
			file.write(html_content.encode('utf8'))

		# Create the images folder
		image_save_folder = os.path.join(save_folder_path, 'images')
		if not os.path.exists(image_save_folder):
			os.makedirs(image_save_folder)


		for i in range(n_image_to_save):
			url = images_info[i]['data-desktop']
			alt = images_info[i].find('img')['alt']

			cur_save_path = os.path.join(image_save_folder, '{}.jpg'.format(image_id))
			cur_image = Image.open(urllib.request.urlopen(url))
			cur_image.save(cur_save_path)
			image_id += 1
			images.append({'image': cur_save_path,
						   'alt': alt})
		hotel_meta['images'] = images

		# Save hotel images

		# Get description
		try:
			hotel_meta['description'] = soup.find('div', {"class": "tagline"}).text.rstrip().lstrip()
		except:
			hotel_meta['description'] = ''
		# Get hotel features
		try:
			main_amenities = soup.find('div', {"data-overview-section-type": "HOTEL_FEATURE"}).find_all('li')
			main_amenities = [amenity.text for amenity in main_amenities]
			hotel_meta['main_amenities'] = main_amenities
		except:
			hotel_meta['main_amenities'] = ''

		# Get family friendly features
		try:	
			family_features = soup.find('div', {"data-overview-section-type": "FAMILY_FRIENDLY_SECTION"}).find_all('li')
			family_features = [feature.text for feature in family_features]
			hotel_meta['family_features'] = family_features
		except:
			hotel_meta['family_features'] = ''	

		# Get whats around
		try:	
			whats_around = soup.find('div', {"data-overview-section-type": "LOCATION_SECTION"}).find_all('li')
			whats_around = [item.text for item in whats_around]
			hotel_meta['whats_around'] = whats_around
		except: 
			hotel_meta['whats_around'] = ''

		# Get room and price information
		rooms = []
		# try:
		all_room_info = soup.find('ul', {"class": "rooms"}).find_all('li', {"class", "room"})

		## Go over rooms and cache the information
		for room_info in all_room_info:

			# Get room name
			room_name = room_info.find('span', {"class": "room-name"}).text

			# Get room image and save it
			try:
				hotel_image_url = room_info.find('a', {"class": "room-images-link"})['href']
				room_image = Image.open(urllib.request.urlopen(hotel_image_url))
				room_image_save_path = os.path.join(image_save_folder, '{}.jpg'.format(image_id))
				room_image.save(room_image_save_path)
			except:
				room_image_save_path = ''
			image_id += 1


			# Get the bed information
			try:
				bed_type = room_info.find('div', {"class": "room-and-hotel-info"})
				bed_type = bed_type.find('ul').text
			except:
				bed_type = ''

			# Get price
			room_price = room_info.find('div', {"class": "price"}).text

			# Cache room information
			rooms.append({'room_name': room_name,
						 'room_image': room_image_save_path,
						 'bed_type': bed_type,
						 'price': room_price})
		# except:
		# 	rooms = []

		hotel_meta['rooms'] = rooms

# Save hotel meta
	#print(hotel_meta)

	

		meta_save_path = os.path.join(save_folder_path, 'meta.pkl')
		with open(meta_save_path, 'wb') as file:
			pickle.dump(hotel_meta, file)
			print(hotel_meta)
			
	except:
		print('Could not load information for hotel {}'.format(hotel_name))



	



if __name__ == '__main__':
	# Testing the function
	check_in = '2020-08-16'
	check_out = '2020-08-17'
	address_template = 'https://www.hotels.com/search.do?&q-destination={}&q-check-in={}&q-check-out={}&q-rooms=1&q-room-0-adults=2&q-room-0-children=0'
	# Root folder for saving the hotel data
	root_save_folder = 'hotel_data'

	# Hotel names you want to get the data for
	hotel_names = ['Holiday Inn Resort Beach House', 'Fitzpatrick Grand Central']
	for hotel_name in hotel_names:
		save_hotel_info(hotel_name, address_template, check_in, check_out, root_save_folder)


