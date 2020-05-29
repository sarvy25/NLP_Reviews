<p align="center"><b>Sarvenaz Memarzadeh</b></p>
<p align="center">sarvenaz.me@gmail.com</p>

# Hotel Reviews Analysis Using Natural Language Processing

## Table of Contents
1. [Problem](README.md#problem)
2. [Dataset](README.md#dataset)
3. [Approach](README.md#approach)
4. [User interface](README.md#approach)

## Problem
How does customer review impact on your business? 

**The goal is to analyze cutomer reviews of hotels and classify their comments into positive, neutral and negative using natural language processing.**

## Dataset
The dataset contains the hotel reviews are from the Kaggle website which you can find it <a href="https://www.kaggle.com/datafiniti/hotel-reviews">here</a>. The rest of the data are collected by web scrapping using the hotelsComScraper.py file. 
This file contains a function called ```save_hotel_info``` which uses beautifulsoup to parse the webpage contents. It goes over each number of hotels get the input of
```hotel_name```, ```address_template```, ```check_in```, ```check_out```, ```root_save_folder```, ```sleep_between_queries=0```, ```max_images_per_hotel=5``` and save the hotel information including the images, description of hotels, main amenities, family features, whats around, room name,
bed type and price in a meta dictionary. 


## Approach
The app is implemented in Python. It is compatible with Python3. 

A function called ```return_reviews``` is implemented which gets the hotel name as the input and returns its reviews by classifying them into positive, negative and neutral. It also returns the ```Sarvy's star``` which is computed by taking the average over the predicted values. 
Sentiment analysis is performed in the hotel_sentiment which gets the csv file in a data frame format, state name, hotel name, model,and reviews. Each review is converted into its feature matrix using the CountVectorizer function from the nltk library. 

## User interface
<p align="center">
<img src="https://github.com/sarvy25/NLP_Reviews/raw/master/github_images/main_search.png" />
</p>


<p align="center">
<img src="https://github.com/sarvy25/NLP_Reviews/raw/master/github_images/review_samples.png" />
</p>
