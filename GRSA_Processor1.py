'''This is the main processor core for our GRSA1.0 software.'''
'''The entire program should be run by calling this.py'''

import ReviewHarvester as RH
import SentimentAnalyzer as SA
import pandas as pd

#Can I add grab a game image with the scraper also?

#UI request should be input as this string.
#Check the Database for GameID or GameName Here
url = input("Add your Steam URL here:")
GameName = (url.split('/')[-2])
ID = (url.split('/')[-3])
print(ID, GameName)


#If the GameID is not found in database, then run Analysis().

def GameData():
    RH.ReviewHarvester(ID)
    SA.SA()
GameData()

#export = For URL/GameID add Analysis() to database


#Translate SA results.
#clean SA results.

'''UI Output:

Flask?: https://realpython.com/python-web-applications/#choose-a-hosting-provider-google-app-engine
or: https://blog.pythonanywhere.com/169/
Project Directory: https://flask.palletsprojects.com/en/2.0.x/tutorial/layout/

Output top/bottom reviews or 'sentiments'? Could use a word cloud or list?
#Patrick working on PowerBI Dashboard output?
#graphical output via matplotlib?
#Send Output to UI.''' 

