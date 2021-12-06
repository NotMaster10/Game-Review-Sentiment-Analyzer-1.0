from flask import Flask, render_template, request
import SentimentAnalyzer as SA
import pandas as pd
import game_data as gd

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
   Gamedata = gd.GameData("NLTK")
   return render_template("index.html", GameData=Gamedata)

@app.route("/about")
def about():
   return render_template("about.html")

@app.route("/help")
def helpme():
   return render_template("help.html")

    
@app.route("/result", methods = ['POST'])
def result():
    output = request.form['url']
    #print(output)
    try:
        GameName = (output.split('/')[-2])
        ID = (output.split('/')[-3])
    except IndexError:
        return render_template("error.html")
    #print(ID, GameName)
    
    feedback = SA.SA(ID)
    CompoundAvg = pd.DataFrame.mean(feedback['Compound'])
    
    def textScore ():
        Description = ""
        if -1.0 < CompoundAvg and -0.8 >= CompoundAvg:
            TextScore = "1  Failure"
            return TextScore
        elif -0.8 < CompoundAvg and -0.6 >= CompoundAvg:
            TextScore = "2  Bad"
            return TextScore
        elif -0.6 < CompoundAvg and -0.4 >= CompoundAvg:
            TextScore = "3  Poor"
            return TextScore
        elif -0.4 < CompoundAvg and -0.2 >= CompoundAvg:
            TextScore = "4  Below Average"
            return TextScore
        elif -0.2 < CompoundAvg and 0.0 >= CompoundAvg:
            TextScore = "5  Mediocre"
            return TextScore
        elif 0.0 < CompoundAvg and 0.2 >= CompoundAvg:
            TextScore = "6  It's okay"
            return TextScore
        elif 0.2 < CompoundAvg and 0.4 >= CompoundAvg:
            TextScore = "7  Good"
            return TextScore
        elif 0.4 < CompoundAvg and 0.6 >= CompoundAvg:
            TextScore = "8  Great"
            return TextScore
        elif 0.6 < CompoundAvg and 0.8 >= CompoundAvg:
            TextScore = "9  Superb"
            return TextScore
        elif 0.8 < CompoundAvg and 1.0 >= CompoundAvg:
            TextScore = "10  Flawless"
            return TextScore
    TextScore = textScore()    

    def scoreDescription ():
        Description = ""
        if TextScore == "1  Failure":
            Description = "This game was created with no depth and no talent."
            return Description
        elif TextScore == "2  Bad":
            Description = "Any good this game had is quickly swallowed up by a plethora of issues."
            return Description 
        elif TextScore == "3  Poor":
            Description = "Somewhere this game went wrong. The original idea might have had promise, but in practice it failed."
            return Description
        elif TextScore == "4  Below Average":
            Description = "This game may have its high points but they soon give way to its glaring faults."
            return Description
        elif TextScore == "5  Mediocre":
            Description = "This game is an excercise in apathy. Neither hot nor cold. Simply mediocre."
            return Description
        elif TextScore == "6  It's okay":
            Description = "This game is slightly above average, or else just inoffensive."
            return Description
        elif TextScore == "7  Good":
            Description = "There could be some irritating faults to the game, but overall it's fun to play."
            return Description
        elif TextScore == "8  Great":
            Description = "Game devs made an impressive effort. The game has few noticable problems. It may not everyone's cup of tea, but many will enjoy it."
            return Description
        elif TextScore == "9  Superb":
            Description = "This game is the hallmark of excellence. It migh have a few flaws but they are negligable."
            return Description
        elif TextScore == "10  Flawless":
            Description = "This game is as perfect as you can get in its given genre."
            return Description
    Description = scoreDescription()
    #Attempt to grab GameNews using API
    Gamedata = gd.GameData(GameName)
    print(Gamedata)
    return render_template('index.html', GameName=GameName, Score=TextScore, ScoreText=Description, GameData=Gamedata)
   
   
    #export = For URL/GameID add Analysis() to database
    #Pull Game ID output from database
    
if __name__ == '__main__':
   app.run(debug = True,port=5001)
   
   
'''
Flask: https://realpython.com/python-web-applications/#choose-a-hosting-provider-google-app-engine
Project Directory: https://flask.palletsprojects.com/en/2.0.x/tutorial/layout/
'''

