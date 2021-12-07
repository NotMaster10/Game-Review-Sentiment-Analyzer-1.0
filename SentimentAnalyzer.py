
"""
If you use the VADER sentiment analysis tools, please cite:

Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for
Sentiment Analysis of Social Media Text. Eighth International Conference on
Weblogs and Social Media (ICWSM-14). Ann Arbor, MI, June 2014.
"""
#import nltk
#import nltk.data
import pandas as pd
import ReviewHarvester as RH
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def SA(GID):
    new_words = {'running hot': -3.0,}

    sia = SentimentIntensityAnalyzer()
    sia.lexicon.update(new_words)
    
    df1 = RH.ReviewHarvester(GID)
    df2 = df1['Reviews']
    
    df1['Compound'] = [sia.polarity_scores(x)['compound'] for x in df2]
    df1['Neg'] = [sia.polarity_scores(x)['neg'] for x in df2]
    df1['Neu'] = [sia.polarity_scores(x)['neu'] for x in df2]
    df1['Pos'] = [sia.polarity_scores(x)['pos'] for x in df2]
    return(df1) 

if __name__ == '__main__':
    sys.exit(main())