# Project 1 mmp224

## Milestone 1 questions:
### What are at least 3 technical issues you encountered with your project? How did you fix them?
- When trying to fetch the json data for an artists, I initially kept recieving an error with status 401 and it took me some time to realize that I had to get something called and OAuth Token, which ended up fixing the issue.
- And speaking of fetching the json data, in order to print specifics like the song name, artists name, etc. the json that I printed to check was not at all readable to the eyes, and not formatted correctly. I fixed the problem by writing the json data to a random text file so that I could look at it in a proper format. 
- And lastly, although it seems to be a little issue that occured since homework 4 I'd still like to point it out, that just saving the css file doesn't make changes to the final result. In order to fix the issue I kept having to rename the css file in order for the changes to show up. 

### What are known problems (still existing), if any, with your project?
- None

### What would you do to improve your project in the future?
- At this point after completing milestone 1, the main thing to improve would be how the html page looks. Making it pleasing to the eye with better placement, font, and a message telling the user there's no audio preview if it seems to be the case.

### Technologies:
- Cloud9

### Framework:
- Flask

### Libraries:
- from flask import Flask, render_template
- import os
- import random
- import requests
- from dotenv import load_dotenv, find_dotenv
- import json 

### APIs:
- Spotify

### Setting up the project:
