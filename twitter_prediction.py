import tweepy
from textblob import TextBlob

def getSentimentAnalysis(tweets):
	p = 0
	i = 0
	for tweet in tweets:
	    analysis = TextBlob(tweet.text)
	    p = analysis.sentiment.polarity + p
	    i = i + 1
	return p / i

consumer_key= 'CxBK8Kt9F7D23JyYlZd8E6eLP'
consumer_secret= 'yVvxnYvso8trbvo4kLZLZmFmjasVITpbszFEw8cqUjW2o6KRys'

access_token='303531438-w7mH7Nf1cMVGIJdGgeffF5Y730tkpHuFNw9zsLFu'
access_token_secret='RUMmfv6isJ9ZgaEXseW9g8J9TBfOgvXC3gPkO2dUwA7GT'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

mcdonalds = api.search('mcdonalds')
burger_king = api.search('burger king')
kfc = api.search('KFC')
taco_bell = api.search('taco bell')
starbucks = api.search('starbucks')

print("mcdonalds: "+ str(getSentimentAnalysis(mcdonalds)))
print("burger king: "+ str(getSentimentAnalysis(burger_king)))
print("kfc: "+ str(getSentimentAnalysis(kfc)))
print("taco bell: "+ str(getSentimentAnalysis(taco_bell)))
print("starbucks: "+ str(getSentimentAnalysis(starbucks)))



