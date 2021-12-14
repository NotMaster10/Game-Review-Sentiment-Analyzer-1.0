
"""
Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for
Sentiment Analysis of Social Media Text. Eighth International Conference on
Weblogs and Social Media (ICWSM-14). Ann Arbor, MI, June 2014.
"""

import pandas as pd
import os
import sys
import pickle
import ReviewHarvester as RH
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

#print(os.listdir('.'))
os.chdir( os.path.dirname( sys.argv[0] ) )

def SA(GID):
    
    #with open('lexicon.txt', 'rb') as doc:
        #print(doc)
        #new_words = pickle.loads( doc )  <---Hitting an error here. I think it has to do with that I need to recreate into a new dictionary within this module to use that dict.
    #    print(new_words)
        
    #for key, value in new_words.items():
    #    if value == 0:
    #       del new_words[key]

    sia = SentimentIntensityAnalyzer()
    #sia.lexicon.update(new_words)
    
    df1 = RH.ReviewHarvester(GID)
    df2 = df1['Reviews']
    
    df1['Compound'] = [sia.polarity_scores(x)['compound'] for x in df2]
    df1['Neg'] = [sia.polarity_scores(x)['neg'] for x in df2]
    df1['Neu'] = [sia.polarity_scores(x)['neu'] for x in df2]
    df1['Pos'] = [sia.polarity_scores(x)['pos'] for x in df2]
    return(df1) 

if __name__ == '__main__':
    sys.exit(main())