'''This is the main processor core for our GRSA1.0 software.'''
'''The entire program should be run by calling this.py'''

#Can I add grab a game image with the scraper also?

import requests    #https://docs.python-requests.org/en/latest/ for API requests with py
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


#Can I add an image scraper to this?
def GRSA():
    url = input("Enter your Steam URL to analyze: ")
    GameID = (url.split('/')[-3])
    GameName = (url.split('/')[-2])
    print(GameID, GameName)

    #if GameID not in Database, then:

    response = requests.get(url=f'https://store.steampowered.com/appreviews/{GameID}?json=1')
   
    '''Return an error code if request unsuccessful'''
    if response.status_code != 200: 
        print('Status:', response.status_code, 'Problem with the request. Exiting.')
        exit()
    
    '''Pulling only the reviews and reviewIDs from the information'''
    data = response.json()
    reviews = []
    reviewIDs = []
    
    field_list = data['reviews']
    for fields in field_list:
        review = (fields['review'])
        reviews.append(review)
        reviewID = (fields['recommendationid'])
        reviewIDs.append(reviewID)
    df = pd.DataFrame({'IDs': reviewIDs, 'Reviews': reviews})
    print(df)

    sia = SentimentIntensityAnalyzer()
    df1 = df['Reviews']
    
    #update the vader lexicon here to include more gaming language
    new_words = {'hot': -3.5,}
    sia.lexicon.update(new_words)


    df['Compound'] = [sia.polarity_scores(x)['compound'] for x in df1]
    df['Neg'] = [sia.polarity_scores(x)['neg'] for x in df1]
    df['Neu'] = [sia.polarity_scores(x)['neu'] for x in df1]
    df['Pos'] = [sia.polarity_scores(x)['pos'] for x in df1]
    
    CompoundAvg = pd.DataFrame.mean(df['Compound'])
    NegAvg = pd.DataFrame.mean(df['Neg'])
    NeuAvg = pd.DataFrame.mean(df['Neu'])
    PosAvg = pd.DataFrame.mean(df['Pos'])

    print(CompoundAvg, NegAvg, NeuAvg, PosAvg)
    
    #Translate SA results.
    #clean SA results.
    
    #if GameID in Database:
    #Return Output
    
    
    
GRSA()

'''UI Output:

Flask?: https://realpython.com/python-web-applications/#choose-a-hosting-provider-google-app-engine
or: https://blog.pythonanywhere.com/169/
Project Directory: https://flask.palletsprojects.com/en/2.0.x/tutorial/layout/

Output top/bottom reviews or 'sentiments'? Could use a word cloud or list?
#Patrick working on PowerBI Dashboard output?
#graphical output via matplotlib?
#Send Output to UI.''' 