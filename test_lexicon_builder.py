'''VG_lexicon_builder 1.1
12/09/21
Hannah Tonce'''

import requests
import pickle
import nltk
from nltk.tokenize import RegexpTokenizer
tokenizer=nltk.RegexpTokenizer(r"\w+")


output = input("Steam URL to pull data from: ")
GameName = (output.split('/')[-2])
GameID = (output.split('/')[-3])
response = requests.get(url=f'https://store.steampowered.com/appreviews/{GameID}?json=1')
#lexicon = dict()

'''If I were rebuilding this I would use TextBlob to train/classify the reviews from there rather than
vaderSentimentAnalyzer as it is more flexibile in allowing for training your data sets yourself, should work
for any set of text data rather than being specific to social media posts and needing updated.'''

data = response.json()
reviews = []
with open('lexicon.txt', 'rb') as file:
    lexicon = pickle.load(file)

    field_list = data['reviews']
    for fields in field_list:
        
        if fields['voted_up'] == True:
            review = tokenizer.tokenize(fields['review'])
   
            for word in review:
                if word in lexicon:
                    lexicon[word] += .01
                else:
                    lexicon[word] = 0
        elif fields['voted_up'] == False:
            review = tokenizer.tokenize(fields['review'])
            for word in review:
                if word in lexicon:
                    lexicon[word] -= .01
                else:
                    lexicon[word] = 0
print(lexicon)

with open ('lexicon.txt', 'wb') as file:
    pickle.dump(lexicon, file)

