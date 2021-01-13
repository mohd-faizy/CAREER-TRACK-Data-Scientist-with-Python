'''
01 - API Authentication

The package tweepy is great at handling  all  the  Twitter API OAuth  Authentication
details for you. All you need to do  is  pass  it  your  authentication  credentials. 
In this interactive exercise, we have created some mock  authentication  credentials 
(if you wanted to replicate this at home, you would need to create a Twitter App  as 
Hugo detailed in the video). Your task is to pass these credentials to tweepy's OAuth 
handler.

Instructions

- Import the package tweepy.
- Pass the parameters consumer_key and consumer_secret to the function tweepy.OAuthHandler().
- Complete the passing of OAuth credentials to the OAuth handler auth by applying to it the
  method set_access_token(), along with arguments access_token and access_token_secret.
'''
# Import package
import tweepy

# Store OAuth authentication credentials in relevant variables
access_token = "1092294848-aHN7DcRP9B4VMTQIhwqOYiB14YkW92fFO8k8EPy"
access_token_secret = "X4dHmhPfaksHcQ7SCbmZa2oYBBVSD2g8uIHXsp5CTaksx"
consumer_key = "nZ6EA0FxZ293SxGNg8g8aP0HM"
consumer_secret = "fJGEodwe3KiKUnsYJC3VRndj7jevVvXbK2D5EiJ2nehafRgA6i"

# Pass OAuth details to tweepy's OAuth handler
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
