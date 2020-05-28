import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from nltk.tokenize import RegexpTokenizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
hotel_name = 'Hotel Zelos'
# this function returns the reviews(positive,negtive, neutral) for each specific hotel's name
def return_reviews(hotel_name):

    csv_path = 'static/data/Datafiniti_Hotel_Reviews.csv'
    df = pd.read_csv(csv_path)
    state_name = 'CA'
    df_state = df[df['province'] == state_name]
    # classify rating in to three classes
    y = df_state['reviews.rating']
    y = y.mask(df_state['reviews.rating'] < 3 , 1) # mask is a function
    y = y.mask(df_state['reviews.rating'] == 3 , 3)
    y = y.mask(df_state['reviews.rating'] > 3 , 5)

    token = RegexpTokenizer(r'[a-zA-Z0-9]+')
    # conveting reviews to vector
    cv = CountVectorizer(lowercase = True, stop_words = 'english', ngram_range = (1,1), tokenizer = token.tokenize)
    feature = cv.fit_transform(df_state['reviews.text'].apply(lambda x: np.str(x))) # featrur vector


    X_train, X_test, y_train, y_test = train_test_split(feature, y.astype('int'), 
                                                       test_size =0.3, random_state = 1)
    # fit model on training data set
    model = MultinomialNB().fit(X_train, y_train)

    def hotel_sentiment(df, state_name, hotel_name, model, cv):
        df_state = df[df['province'] == state_name]
        df_hotel = df_state[df_state['name'] == hotel_name]
        feature = cv.transform(df_hotel['reviews.text'].apply(lambda x: np.str(x))) # feature vector


        # get a single hotel and transform it to the features vector using cv
        y_predicted = model.predict(feature)
        star = sum(y_predicted)/len(y_predicted)

        reviews = df_hotel['reviews.text']
        positive_reviews = []
        negative_reviews = []
        neutral_reviews = []

        for i, review in enumerate(reviews):
            if y_predicted[i] == 5:
                positive_reviews.append(review)
            elif y_predicted[i] == 3:
                neutral_reviews.append(review)
            else:
                negative_reviews.append(review)
#        total_reviews = len(neutral_reviews) + len(positive_reviews) + len(negative_reviews)
#         print('pos:', positive_reviews)
#         print('neg:', negative_reviews)
#         print('neut:', neutral_reviews)

        #star = (5*len(positive_reviews)+3*len(neutral_reviews)+1*len(negative_reviews))/total_reviews
        return positive_reviews, negative_reviews, neutral_reviews, star
    
    return hotel_sentiment(df, state_name, hotel_name, model, cv)

return_reviews(hotel_name)