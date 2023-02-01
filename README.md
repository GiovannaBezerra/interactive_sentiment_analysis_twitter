<img src="https://user-images.githubusercontent.com/44107852/215857260-d6660a43-e731-484c-8645-0512c97776c9.png" align="right"
      width="80" height="80">
      
# INTERACTIVE SENTIMENT ANALYSIS ON TWITTER

This program does a sentiment analysis of text data, entered by the user, to detect its polarity considering the 100 most recent tweets on Twitter. This way it is possible to know if people are talking positively, negatively or neutrally about the subject.

<p align="center">
  <a href="#how-it-works">How it works</a> •
  <a href="#installation-and-configuration">Installation and configuration</a> •
  <a href="#how-to-use">How to use</a> •
  <a href="#notes-and-considerations">Notes and considerations</a> •
</p>

![gif_app_isat](https://user-images.githubusercontent.com/44107852/216171424-85d21322-4c28-452b-87f1-e3070122447e.gif)

## How it Works  

Sentiment analysis is used to identify how people are talking about a given topic by detecting the polarity of text data. In this project was used the **TextBlob** library, which is a natural language processing module, to automatically identify whether a tweet can be categorized as positive, negative or neutral polarity.
Moreover, a user interface was created using PySimpleGUI where the user can enter some keyword and the program returns a **Pie Chart** with the polarity rate and three **Word Clouds** with positive, negative tweets and neutral on the research topic.

We can divide the project into three stages:

1. Get data tweets through Tweepy API
2. Use TextBlob to detect polarity of text data
3. Create user interface using PySimpleGUI


## Installation and configuration 

### Clone this repository
```
git clone xxxxxx
```  
  
### Install development dependencies
```
pip install pandas  
pip install numpy  
pip install tweepy  
pip install -U textblob  
pip install PySimpleGUI  
pip install wordcloud  
pip install matplotlib
pip install PySimpleGUI
```  

### Get Twitter developer credentials

To get developer credentials, you should have a Twitter account.  
  
After, acess the oficial Twitter Developer Portal on https://developer.twitter.com/en/portal/projects-and-apps

In *Projects&Apps* click on *Overview* and then on *+ Create APP*.

<img src="https://user-images.githubusercontent.com/44107852/215882178-50244841-be70-447f-960d-da92b7390cc0.jpg" align="center"
      width="800" height="800">

Name your app and click on *Next*.

![name_app](https://user-images.githubusercontent.com/44107852/215882487-d5f5623a-3cec-47ec-8a5f-9ab856c810e9.jpg)

Now you can see your keys & tokens. Click on *App settings* for more details.

![keys_app_1](https://user-images.githubusercontent.com/44107852/215882674-bdf84722-61b8-4180-a5d4-670620e3714e.jpg)

To get Access Token and Access Token Secret, you should click on *Revoke* Bearer Token and *Generate* Access Token and Secret.

![keys_app_2](https://user-images.githubusercontent.com/44107852/215882920-b9592e03-1cc5-473d-a5ff-dcfd9a249a3f.jpg)

Copy and save your credentials.


## How to use

To start the interactive program open the python file **interactive_sentiment_analysis_twitter.py** in some IDE like VSCode, PyCharm and others.  

...or use terminal to run the program.  

![run_file](https://user-images.githubusercontent.com/44107852/215883432-40ab2c4c-7129-46c8-bf39-5f3dbe1da261.jpg)

Input your Twitter developer credentials and click Continue.

![input_credentials](https://user-images.githubusercontent.com/44107852/215883476-e17b19fc-e35e-421e-adeb-7c3cc1132787.jpg)

Input some keyword and click Search.

![window_search](https://user-images.githubusercontent.com/44107852/215883553-2d29cbaa-dbaa-473f-b2d5-76731cf0741f.jpg)

The three most recents tweets are showed.

Select a visualization and click Plot Visualization.

Pie chart
![pie_chart](https://user-images.githubusercontent.com/44107852/216157872-bb3f1ca0-754d-42e9-9307-4f184bf7518f.jpg)


Positives
![wordcloud_positives](https://user-images.githubusercontent.com/44107852/216157939-a693e962-e3d5-4224-b7c2-253bbcb48687.jpg)





## Notes and Considerations

At this point the TextBlob library works only to analysis in English. So....

During this development, I've learned how to use Dash and Plotly libraries, which was very challenging for me, in particular because of layout building and callbacks construction.
