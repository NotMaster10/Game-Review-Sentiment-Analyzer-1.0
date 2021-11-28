from flask import Flask, render_template, request
import SentimentAnalyzer as SA
import pandas as pd

app = Flask(__name__)
#output = ""
#GameName = 'Game Name'
#ID = 'Steam Game ID'
#Score = 0

@app.route("/")
@app.route("/home")
def home():
   return render_template("index.html")

@app.route("/about")
def about():
   return render_template("about.html")

@app.route("/help")
def helpme():
   return ("help.html")
   
@app.route("/result", methods = ['POST'])
def result():
    output = request.form['url']
    print(output)
    #Set variables GameName and ID
    GameName = (output.split('/')[-2])
    ID = (output.split('/')[-3])
    print(ID, GameName)
    
    feedback = SA.SA(ID)
    
    CompoundAvg = pd.DataFrame.mean(feedback['Compound'])
    #NegAvg = pd.DataFrame.mean(feedback['Neg'])
    #NeuAvg = pd.DataFrame.mean(feedback['Neu'])
    #PosAvg = pd.DataFrame.mean(feedback['Pos'])
    
    #print(feedback)

    '''Here we need to only run the SA, have those results input into a new HTML
    then we can render the new HTML as results.'''
    return render_template('index.html', GameName=GameName, GameID=ID, Score=CompoundAvg)
    #export = For URL/GameID add Analysis() to database

    #Pull Game ID output from database
    
if __name__ == '__main__':
   app.run(debug = True,port=5001)
   
   
'''
Flask: https://realpython.com/python-web-applications/#choose-a-hosting-provider-google-app-engine
Project Directory: https://flask.palletsprojects.com/en/2.0.x/tutorial/layout/
'''

