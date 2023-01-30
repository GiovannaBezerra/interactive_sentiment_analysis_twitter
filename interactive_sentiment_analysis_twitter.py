# Interactive Sentiment Analysis on Twitter

# This sentiment analysis program detects the polarity of text data, entered by the user, 
# considering the 100 most recent tweets on Twitter. This way it is possible to know if 
# people are talking positively, negatively or neutrally about the subject.

# Import modules:
import pandas as pd
import numpy as np
import tweepy
from textblob import TextBlob as tb
from wordcloud import WordCloud
from wordcloud import STOPWORDS
import re
import matplotlib.pyplot as plt
import PySimpleGUI as sg

# Authentication function:
def auth_twitter(api_key,api_key_secret,access_token,access_token_secret):
    """
    Return the connection with Twitter API using developer credentials.
    param. 1: API key (str)
    param. 2: API key secret (str)
    param. 3: Access token (str)
    param. 4: Access token secret (str)
    return: api (tweepy.api.API)
    """
    auth = tweepy.OAuthHandler(api_key, api_key_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    return api

# Function to remove special characters:
def clean_tweet(tweet):
    """
    Return a tweet without special characters.
    param.: tweet (str)
    return: tweet (str)
    """
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|       (\w+:\/\/\S+)", " ", tweet).split())

# Function to classify polarity:
def analize_sentiment(tweet):
    """
    Return the tweet polarity classification: positive, negative or neutral.
    param.: tweet (str)
    return: polarity (str)
    """   
    analysis = tb(clean_tweet(tweet.text))
    if analysis.sentiment.polarity > 0:
       return 'positive'
    elif analysis.sentiment.polarity == 0:
       return 'neutral'
    else:
        return 'negative'

# Function to set a data frame with tweets and polarities:
def dataframe_tweets(api,search_word):
    """
    Return a data frame with tweets and polarities.
    param. 1: api (tweepy.api.API)
    param. 2: search_word (strt)
    return: df (pandas data frame)
    """      
    public_tweets = api.search_tweets(search_word, lang='en', count=100)
    df = pd.DataFrame(data=[tweet.text for tweet in public_tweets], columns=['text_tweets'])
    df['sa'] = np.array([analize_sentiment(tweet) for tweet in public_tweets])
    return df

# Funcion to make pie chart:
def draw_plot(data):
    """
    Return a pie chart with sentiment analysis results of tweets.
    param.: data (pandas data frame)
    return: plt (matplotlib object)
    """      
    plt.figure(num='Pie Chart',figsize=(5,5), dpi=100)
    colors = ['#ff9999','#66b3ff','#99ff99']
    ax = plt.subplot()
    data.plot.pie(ax=ax, autopct='%1.1f%%',startangle=270,fontsize=11,colors=colors,shadow=True)
    plt.title("Sentiment analysis results of tweets",fontsize=16)
    plt.show(block=False)

# Funcion to make positive word cloud:
def draw_wordcloud_positive(df):
    """
    Return a word cloud for positive tweets.
    param.: df (pandas data frame)
    return: plt (matplotlib object)
    """      
    positive_tweets = [tweet for index, tweet in enumerate(df['text_tweets']) if df['sa'][index] == 'positive']
    stop_words = ["https", "co", "RT"] + list(STOPWORDS)
    positive_wordcloud = WordCloud(max_font_size=50, 
                                    max_words=50, 
                                    background_color="white", 
                                    stopwords = stop_words).generate(str(positive_tweets))
    plt.figure(num='Word  Cloud - Positive Tweets')
    plt.title("Word Cloud for positive tweets",fontsize=16)
    plt.imshow(positive_wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show(block=False)

# Funcion to make negative word cloud:
def draw_wordcloud_negative(df):
    """
    Return a word cloud for negative tweets.
    param.: df (pandas data frame)
    return: plt (matplotlib object)
    """ 
    negative_tweets = [tweet for index, tweet in enumerate(df['text_tweets']) if df['sa'][index] == 'negative']
    stop_words = ["https", "co", "RT"] + list(STOPWORDS)
    negative_wordcloud = WordCloud(max_font_size=50, 
                                    max_words=50, 
                                    background_color="white", 
                                    stopwords = stop_words).generate(str(negative_tweets))
    plt.figure(num='Word  Cloud - Negative Tweets')
    plt.title("Word Cloud for negative tweets",fontsize=16)
    plt.imshow(negative_wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show(block=False)

# Funcion to make neutral word cloud:
def draw_wordcloud_neutral(df):
    """
    Return a word cloud for neutral tweets.
    param.: df (pandas data frame)
    return: plt (matplotlib object)
    """ 
    neutral_tweets = [tweet for index, tweet in enumerate(df['text_tweets']) if df['sa'][index] == 'neutral']
    stop_words = ["https", "co", "RT"] + list(STOPWORDS)
    neutral_wordcloud = WordCloud(max_font_size=50,
                                   max_words=50,
                                   background_color="white", 
                                   stopwords = stop_words).generate(str(neutral_tweets))
    plt.figure(num='Word  Cloud - Neutral Tweets')
    plt.title("Word Cloud for neutral tweets",fontsize=16)
    plt.imshow(neutral_wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show(block=False)

# Building layout:
def window_credentials():
    sg.theme('DarkGrey13')
    layout = [
        [sg.Text('Input your Twitter Developer Credentials', size=(40,1), font=('Helvetica',16))],
        [sg.Text('For more information about Twitter Developer Credentials access: https://developer.twitter.com/en/portal/projects-and-apps ', 
            font=('Helvetica',9))],
        [sg.Text('__'*100, size=(90,1))],
        [sg.Text(' '*100,size=(90,1))],
        [sg.Text('API key:',font=('Helvetica',11)),sg.Input(size=(65,1),key='input_api_key')],
        [sg.Text('API key secret:',font=('Helvetica',11)),sg.Input(size=(65,1),key='input_api_key_secret')],
        [sg.Text('Access token:',font=('Helvetica',11)), sg.Input(size=(65,1),key='input_access_token')],
        [sg.Text('Access token secret:',font=('Helvetica',11)), sg.Input(size=(65,1),key='input_access_token_secret')],
        [sg.Text(' '*100,size=(90,1))],
        [sg.Button('Cancel',size=(15,1),font=('Helvetica',12)), sg.Button('Continue',size=(15,1),font=('Helvetica',12))]
    ]
    return sg.Window('Twitter Credentials', layout=layout, finalize=True)

def window_result():
    sg.theme('DarkGrey13')
    layout=[
        [sg.Text('Input keyword to search:', size=(65,1), font=('Helvetica',12))],
        [sg.Input(key='input_search_word', size=(65,1), font=('Arial',14))],
        [sg.Button('Cancel',size=(15,1),font=('Helvetica',12)), 
            sg.Button('Back',size=(15,1),font=('Helvetica',12)), 
            sg.Button('Search',size=(15,1),font=('Helvetica',12))
            ],
        [sg.Text('See three recent tweets:'+'__'*100,size=(100,1),font=('Helvetica',11))],
        [sg.Text(size=(100,1),key='-output1-',text_color='MediumPurple')],
        [sg.Text(size=(100,1),key='-output2-',text_color='MediumPurple')],
        [sg.Text(size=(100,1),key='-output3-',text_color='MediumPurple')],
        [sg.Text('__'*100, size=(112,1))],
        [sg.Radio('Show Pie Chart',key='piechart',default=True,group_id='1',size=(15,1),font=('Helvetica',11)),
            sg.Radio('Show Positive Word Cloud',key='positive',group_id='1',size=(20,1),font=('Helvetica',11)),
            sg.Radio('Show Negative Word Cloud',key='negative',group_id='1',size=(20,1),font=('Helvetica',11)),
            sg.Radio('Show Neutral Word Cloud',key='neutral',group_id='1',size=(20,1),font=('Helvetica',11)),  
        ],
        [sg.Button('Plot visualization',size=(25,1),font=('Helvetica',12))]
    ]
    return sg.Window('Search Keyword', layout=layout, finalize=True)


# Building windows:
window_1, window_2 = window_credentials(), None

# Creating events loop:
while True:
    window, event, values = sg.read_all_windows()
    if window == window_1 and event in (sg.WIN_CLOSED, 'Cancel'):
        break
    elif window == window_1 and event == 'Continue':
        window_2 = window_result()
        window_1.hide()
        api_key = values['input_api_key']
        api_key_secret = values['input_api_key_secret']
        access_token = values['input_access_token']
        access_token_secret = values['input_access_token_secret']
        auth_twitter(api_key,api_key_secret,access_token,access_token_secret)
    elif window == window_2 and event in (sg.WIN_CLOSED, 'Cancel'):
        break
    elif window == window_2 and event == 'Back':
        window_2.hide()
        window_1.un_hide()
    elif window == window_2 and event == 'Search':
        search_word = values['input_search_word']
        api = auth_twitter(api_key,api_key_secret,access_token,access_token_secret)
        df = dataframe_tweets(api,search_word)
        sentiment_counts = df.groupby(['sa']).size()
        window['-output1-'].update(df.values[0,0])
        window['-output2-'].update(df.values[1,0])
        window['-output3-'].update(df.values[2,0])
    elif window == window_2 and event == 'Plot visualization':
        if values['piechart'] == True:
            draw_plot(sentiment_counts)
        elif values['positive'] == True:
            draw_wordcloud_positive(df)
        elif values['negative'] == True:
            draw_wordcloud_negative(df)
        elif values['neutral'] == True:
            draw_wordcloud_neutral(df)
    
# Close the window:
window.close()



