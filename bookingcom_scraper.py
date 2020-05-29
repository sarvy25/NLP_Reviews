from bs4 import BeautifulSoup
import urllib
import os
from PIL import Image
address = 'https://www.booking.com/searchresults.html?label=gen173nr-1FCAEoggI46AdIM1gEaJkCiAEBmAExuAEHyAEM2AEB6AEB-AECiAIBqAIDuALf-7j0BcACAQ&sid=f5255735c09dd4dac226c0f4b707ea52&sb=1&sb_lp=1&src=index&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Findex.html%3Flabel%3Dgen173nr-1FCAEoggI46AdIM1gEaJkCiAEBmAExuAEHyAEM2AEB6AEB-AECiAIBqAIDuALf-7j0BcACAQ%3Bsid%3Df5255735c09dd4dac226c0f4b707ea52%3Bsb_price_type%3Dtotal%26%3B&ss=San+Francisco%2C+California%2C+United+States&is_ski_area=&checkin_year=2020&checkin_month=6&checkin_monthday=1&checkout_year=2020&checkout_month=6&checkout_monthday=6&group_adults=2&group_children=0&no_rooms=1&b_h4u_keep_filters=&from_sf=1&ss_raw=san+Francisco&ac_position=0&ac_langcode=en&ac_click_type=b&dest_id=20015732&dest_type=city&iata=SFO&place_id_lat=37.787804&place_id_lon=-122.407503&search_pageview_id=092194efa1200115&search_selected=true&search_pageview_id=092194efa1200115&ac_suggestion_list_length=5&ac_suggestion_theme_list_length=0'
save_image_folder = 'data/images'

if not os.path.exists(save_image_folder):
	os.makedirs(save_image_folder)

f = urllib.request.urlopen(address)
content = f.read()
soup = BeautifulSoup(content, 'html.parser')
all_hotel_divs = soup.find_all('div', {"class": "sr_property_block"}) # output is a list
for hotel_info in all_hotel_divs:
	hotel_name = hotel_info.find_all('span', {"class": 'sr-hotel__name'})[0] # name of hotels
	hotel_name = hotel_name.text.rstrip().lstrip()


	# Save the image
	file_name = hotel_name.replace('/', '').replace(' ', '').lower()
	print(file_name)
	hotel_image_url = hotel_info.find_all('img', {"class": 'hotel_image'})[0] # image of hotels(is a dictionary)

	hotel_image = Image.open(urllib.request.urlopen(hotel_image_url['src']))

	#saving 
	save_path = os.path.join(save_image_folder, file_name + '.png')
	hotel_image.save(save_path)

