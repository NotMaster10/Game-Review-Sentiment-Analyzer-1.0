import urllib.request as urlreq
import re
import random

def GameData(Name):

    #Name = input("What is your search?")
    html = urlreq.urlopen(f"https://www.youtube.com/results?search_query={Name}")
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    vidID = random.choice(video_ids)
    Video = ("https://www.youtube.com/embed/" + vidID)
    return(Video)

if __name__ == '__main__':
    sys.exit(main())