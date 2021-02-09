'''
Mann Patel
UCID: mmp224
Project 1
'''
from flask import Flask, render_template
import os
import random
import requests
from dotenv import load_dotenv, find_dotenv
import json 

app = Flask(__name__)
@app.route('/')
def spotify_API():
    AUTH_URL = 'https://accounts.spotify.com/api/token'
                         #Logic                  The Weeknd                 Travis Scott              21 Savage                Metro Boomin                Big Sean
    artist_ID = ['4xRYI6VqpkE3UwrDrAZL8L', '1Xyo4u8uXC1ZmMpatF05PJ', '0Y5tJX1MQlPlqiwlOH1tJY', '1URnnhqYAYcrqrcwql10ft', '0iEtIxbK0KxaSlF7G42ZOp', '0c173mlxpT3dSFRgMO8XPh']
    random_Artist = random.choice(artist_ID)
    load_dotenv(find_dotenv())
    BASE_url = 'https://api.spotify.com/v1/artists/' + random_Artist + '/top-tracks?market=US'
    
    params = requests.post(AUTH_URL, {
        'grant_type': 'client_credentials',
        'client_id': os.getenv('CLIENT_ID'),
        'client_secret': os.getenv('CLIENT_SECRET'),
    })
    
    auth_response_data = params.json()
    access_token = auth_response_data['access_token']
    
    headers = {
        'Authorization': 'Bearer {token}'.format(token=access_token)
    }
    
    response = requests.get(BASE_url, headers=headers)
    data = response.json()
    
    '''
    print(data)
    format_Json = json.dumps(data, indent=2)
    x = open('bruh.txt', 'w+')
    x.write(format_Json)
    '''
    
    rC = random.randint(0, len(data["tracks"]) - 1)
    
    song_Title  = data["tracks"][rC]["name"]
    artist_Name = data["tracks"][rC]["album"]["artists"][0]["name"]
    image       = data["tracks"][rC]["album"]["images"][0]["url"] 
    preview_Url = data["tracks"][rC]["preview_url"]
    
    return render_template(
        'index.html',
        song_Title = song_Title, 
        artist_Name = artist_Name, 
        image = image, 
        preview_Url = preview_Url
    )
    
app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug=True
)
