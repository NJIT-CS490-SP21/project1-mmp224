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

app = Flask(__name__)   #instance for flask
@app.route('/')         #python decorater, conncets this route/url with the function

def spotify_API():
    AUTH_URL = 'https://accounts.spotify.com/api/token'     #The endpoint for the API provider authorization server
    
                         #Logic                  The Weeknd                 Travis Scott              21 Savage                Metro Boomin                Rich Brian
    artist_ID = ['4xRYI6VqpkE3UwrDrAZL8L', '1Xyo4u8uXC1ZmMpatF05PJ', '0Y5tJX1MQlPlqiwlOH1tJY', '1URnnhqYAYcrqrcwql10ft', '0iEtIxbK0KxaSlF7G42ZOp', '2IDLDx25HU1nQMKde4n61a']
    random_Artist = random.choice(artist_ID)
    
    load_dotenv(find_dotenv())      #looks for any env file in current directory
    BASE_url = 'https://api.spotify.com/v1/artists/' + random_Artist + '/top-tracks?market=US'  #Base endpoint
    BASE_url_2 = 'https://api.spotify.com/v1/artists/' + random_Artist
    
    #POST request with client credentials, saves the responses
    params = requests.post(AUTH_URL, {
        'grant_type': 'client_credentials',
        'client_id': os.getenv('CLIENT_ID'),
        'client_secret': os.getenv('CLIENT_SECRET'),
    })
    
    #converts response to JSON
    auth_response_data = params.json()
    #saves access token
    access_token = auth_response_data['access_token']
    
    #acess endpoints, sending GET request to API server
    headers = {
        'Authorization': 'Bearer {token}'.format(token=access_token)
    }
    
    #request.get fetches the data, Base url is the end point, headers for acess token
    response = requests.get(BASE_url, headers=headers)
    data = response.json()  #converts response to JSON 
    
    response_2 = requests.get(BASE_url_2, headers=headers)  #for second url (artist image)
    data_2 = response_2.json()                              
    
    rC = random.randint(0, len(data["tracks"]) - 1)
    
    song_Title      = data["tracks"][rC]["name"]
    artist_Name     = data["tracks"][rC]["album"]["artists"][0]["name"]
    image           = data["tracks"][rC]["album"]["images"][0]["url"]
    artist_image    = data_2['images'][0]["url"] 
    preview_Url     = data["tracks"][rC]["preview_url"]
    
    #Genius Connection
    genius_AccessToken = os.getenv("CLIENT_ACCESS_TOKEN_GENIUS")
    BASE_url_3 = 'https://api.genius.com'
    genius_Headers = { 'Authorization': 'Bearer ' + genius_AccessToken }
    genius_Url = BASE_url_3 + '/search'
    genius_Data = {'q': song_Title + ' ' + artist_Name}
    response_3 = requests.get(genius_Url, data = genius_Data, headers = genius_Headers)
    data_3 = response_3.json()
    genius_Lyrics = data_3['response']['hits'][0]['result']['url']
    
    '''
    print(genius_AccessToken)
    print(data_3)
    format_Json = json.dumps(data_3, indent=2)
    x = open('bruh.txt', 'w+')
    x.write(format_Json)
    '''
    
    #translate to html file
    return render_template(
        'index.html',
        song_Title = song_Title, 
        artist_Name = artist_Name, 
        image = image,
        artist_image = artist_image,
        preview_Url = preview_Url,
        genius_Lyrics = genius_Lyrics
    )
    
app.run(
    port=int(os.getenv('PORT', 8080)),  #confirms running on the right port
    host=os.getenv('IP', '0.0.0.0'),    #setting it up to be externally visible
    debug=True                          #restarts server whenever code changes 
)
