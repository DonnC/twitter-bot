#! C:\Python36\python.exe
# twitterbot >> my first twitter bot

import tweepy
import requests
import bs4
import time
import sys
from random import choice
import os
from apixu.client import ApixuClient, ApixuException
from credentials import *
import json

# Set up OAuth and integrate with API
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

DELAY     = 240                         # tweet at 6 mins interval
tweet_to  = 'BrightonThanda'
last_tweet = None                       # lets assume we have none last tweets *as we havent post a pic yet
os.chdir('Images')                      # navigate to images folder

def img_tweet():
    '''
        tweet image and text too to 'tweet_to'
        once every 'DELAY' sec
    '''

    global last_tweet
    global DELAY
    global tweet_to

    images = os.listdir()                                # returns a list of all the pics in the folder
    chat   = ['All men are born equal but a few become', 'Let your creative juices flow and dont be afraid to take chances! - Joel Comm', 'Nearly 60% of terrorists graduated school with degrees in engineering', 'Life doesnt get easier or more forgiving; we get stronger and more resilient',\
              'The simplest things are often the truest', 'The simple act of paying positive attention to people has a great deal to do with productivity',\
              'Less is More.', 'The secret of success is sincerity', 'Many can argue - not many converse','The secret of my success is a two word answer: Know people.']
    recent_tweet = api.user_timeline(tweet_to)[0]       # get the most recent tweet by the user
    print("TWEET I.D: ", recent_tweet.id)

    if recent_tweet != last_tweet:
        # tweet a pic to 'tweet_to'
        pic  = choice(images)
        txt = choice(chat)
        hash_tags = '#Engineers #python @donix_22 #My_twitterbot #twimbos #Chiredzi'
        text = "@{to} {chat} {tags}".format(to = tweet_to, chat = txt, tags = hash_tags)

        try:
            api.update_with_media(filename = pic, status = text)
            print("Tweeted the image: ", pic)

        except Exception as e:
            print("Error posting tweet ", e)

    # update the last tweet to the one we have just tweeted
    last_tweet = recent_tweet

running = True

# lets run the programme
while running:
    try:
        img_tweet()
        print("[*] Tweeted!")
        time.sleep(DELAY)

    except KeyboardInterrupt:
        print("[!] You cancelled 'twitter_bot' operation")
        running = False
