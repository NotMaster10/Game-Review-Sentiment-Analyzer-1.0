#GRSA 1.0 Processor Core
# Hannah Tonce


import SentimentAnalyzer as SA
#import pandas as pd

#Can I add grab a game image with the scraper also?

url = input("Add your Steam URL here:")
GameName = (url.split('/')[-2])
ID = (url.split('/')[-3])
print(ID, GameName)

#If the GameID is not found in database, then run Analysis().

def GameData():
    SA.SA(ID)
GameData()

#export = For URL/GameID add Analysis() to database


#Translate SA results.
#clean SA results.

'''UI Output:

Flask?: https://realpython.com/python-web-applications/#choose-a-hosting-provider-google-app-engine
or: https://blog.pythonanywhere.com/169/
Project Directory: https://flask.palletsprojects.com/en/2.0.x/tutorial/layout/

Output top/bottom reviews or 'sentiments'? Could use a word cloud or list?
#graphical output via matplotlib?
#Send Output to UI.''' 

