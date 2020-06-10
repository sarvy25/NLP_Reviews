<p align="center"><b>Sarvenaz Memarzadeh</b></p>
<p align="center">sarvenaz.me@gmail.com</p>

# Hotel Reviews Analysis Using NLP 

## Table of Contents
1. [Problem](README.md#problem)
2. [Dataset](README.md#dataset)
3. [Approach](README.md#approach)
4. [User interface](README.md#approach)

## Problem
How does customer review impact on your business? 

**The goal is to analyze cutomer reviews of hotels and classify their comments into positive, neutral and negative using machine learning and natural language processing.**

## Dataset
The dataset contains the hotel reviews are from the Kaggle website which you can find it <a href="https://www.kaggle.com/datafiniti/hotel-reviews">here</a>. The rest of the data are collected by web scrapping using the hotelsComScraper.py file. 
This file contains a function called ```save_hotel_info``` which uses beautifulsoup to parse the webpage contents. It goes over each number of hotels get the input of
```hotel_name```, ```address_template```, ```check_in```, ```check_out```, ```root_save_folder```, ```sleep_between_queries=0```, ```max_images_per_hotel=5``` and save the hotel information including the images, description of hotels, main amenities, family features, whats around, room name,
bed type and price in a meta dictionary. 


## Approach
The app is implemented in Python. It is compatible with Python3. 

A function called ```return_reviews``` is implemented which by using the hotel name returns the reviews and classifies them into positive, negative and neutral. It also returns the ```Sarvy's star``` which is computed according to the average of the predicted stars. 
Sentiment analysis is performed in the ```hotel_sentiment``` using the csv file in a data frame format, state name, hotel name, model,and reviews. Each review is then converted into its feature matrix using the CountVectorizer in nltk library. 

## User interface
The main website's template is adopted from <a href="https://colorlib.com/wp/templates/">colorlib</a> webpage. It is modified according to the user's given input by placing a search box which enables the user to search for the hotel's name.  App.py file renders the template according to a certain given hotel's name and once the request is posted it calls the hotel's webpage (hote_page.html) by extracting the images, reviews, price,and the computed star (from the sentiment analysis) from the hotels meta dataset. There is also an autocomplete feature which helps the user to post the name faster.  
<p align="center">
<img src="https://github.com/sarvy25/NLP_Reviews/raw/master/github_images/main_search.png" />
</p>


<p align="center">
<img src="https://github.com/sarvy25/NLP_Reviews/raw/master/github_images/review_samples.png" />
</p>
