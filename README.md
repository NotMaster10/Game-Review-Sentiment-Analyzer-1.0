# Game-Review-Sentiment-Analyzer-1.0
# August-December 2021 
# Created Using Python 3.10
# Flask, NLTK, vaderSentiment, pandas, 


How To Run GRSA 1.0 From PowerShell(Windows):

1. Preparing your environment.
   - https://www.python.org/downloads/ Install Python version 3.10
   - In start menu, type powershell.
   - Open Powershell.
   - Install the required modules using the Powershell cmdlets:
     - "pip install flask"
     - "pip install pandas"
     - "pip install vaderSentiment"
     - "pip install requests"
2. Download the program files from Github. 
   - Click on the green "Code" button and selecting "Download ZIP". 
   - Place the folder containing GRSA 1.0 files where you want it to be housed on your computer.
   - Right-click on the zipped folder and select "Extract All". Click "Extract".
   - If you get an error or don't see the Extract option, you may need to install 7zip: https://www.7-zip.org/.
3. Start the program:
   - Select the app.py file in the GRSA 1.0 folder on your desktop. Right-click and open "properties".
   - Copy the "Location" field from this properties information.
   - In Powershell type "Python " <-- Don't forget to add the space after "Python". 
   - Press ctrl+v to add program location.
   - Type "\app.py" after the program location.
   - Hit Enter to run the program.
4. Using GRSA 1.0 
   - In your browser type "localhost:5001" to access the User Interface.
   - Copy/paste the URL from the game you're interested in from the Valve store website: https://store.steampowered.com/ into the URL field of the GRSA user interface.
   - Click Submit.



FAQs:

1. How did we score the user sentiments: 
The overall sentiment score we translated into a 1-10 numbered scale modeled after the scoring system used by destructoid.com 
reviewers found here: https://www.destructoid.com/the-official-destructoid-review-guide/. Our translated scale is as follows:

   - Score				Description
   - 1 Failure: 		This game was created with or requires no depth and no talent.
   - 2 Bad: 			Any good this game had is quickly swallowed up by a plethora of issues.
   - 3 Poor: 			Somewhere this game went wrong. The original idea might have had promise, but in practice it failed.
   - 4 Below Average: 	This game may have its high points but they soon give way to its glaring faults.
   - 5 Mediocre: 		This game is an excercise in apathy. Neither hot nor cold. Simply medicore.
   - 6 It's okay: 		This game is slightly above average, or else just inoffensive.
   - 7 Good: 			There could be some irritating faults to the game, but overall it's fun to play.
   - 8 Great: 			Game devs made an impressive effort. The game has few noticable problems. It may not be everyone's cup of tea, but many will enjoy it.
   - 9 Superb: 			This game is the hallmark of excellence. It might have a few flaws but they are negligable.
   - 10 Flawless: 		This game is as perfect as you can get in its given genre.

2. What is natural language processing?

3. How does this project use NLTK differently?

4. What is a lexicon?

5. 


References:

"""
Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for
Sentiment Analysis of Social Media Text. Eighth International Conference on
Weblogs and Social Media (ICWSM-14). Ann Arbor, MI, June 2014.
"""