import tweepy
import configparser

#read config file
config= configparser.ConfigParser()
config.read(r"C:\Users\sriva\OneDrive\Desktop\Open-source\Twitter-joke bot\config.cfg")

api_key=config['twitter']['api_key']
api_key_secret=config['twitter']['api_key_secret']

Access_Token=config['twitter']['Access_token']
Access_Token_Secret=config['twitter']['Access_Token_Secret']

#authenticaton

auth= tweepy.OAuthHandler(api_key,api_key_secret)
auth.set_access_token(Access_Token,Access_Token_Secret)

api=tweepy.API(auth)

public_tweets=api.home_timeline()

print(public_tweets)