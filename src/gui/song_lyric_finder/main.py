'''
Developed by: Calinescu Mihai
Date: 8 Apr, 2021

Github: https://github.com/CMihai99
'''


import eel
import requests

eel.init('web')

# Get Song Lyrics
@eel.expose
def test(artist, song):
    url = "https://api.lyrics.ovh/v1/"+artist+"/"+song
    webdata = requests.get(url)
    data = webdata.json()
    lyrics = data['lyrics']
    print(lyrics)

eel.start('index.html', size=(400, 400)) # Open browser window