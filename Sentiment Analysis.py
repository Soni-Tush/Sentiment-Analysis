#!/usr/bin/env python
# coding: utf-8

# In[2]:


# import library
import tweepy
from textblob import TextBlob
from wordcloud import WordCloud
import configparser
import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')


# In[3]:


# read configs
config = configparser.ConfigParser()
config.read('config.ini')
# Twitter API credentials
api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']
access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']


# In[4]:


# Create the authentication object
auth = tweepy.OAuthHandler(api_key, api_key_secret)
# Set the access token and access token secret
auth.set_access_token(access_token, access_token_secret)
# Create the API object while passing in the auth information
api = tweepy.API(auth,wait_on_rate_limit = True)


# In[5]:


# Extract 100 tweets from the twitter user
posts = api.user_timeline(screen_name = "elonmusk",count = 1000,tweet_mode = 'extended')


# In[ ]:


print("Show the 5 recent Tweets: \n")
i=1
for tweet in posts[0:5]:
    print(str(i)+' ) '+tweet.full_text + '\n')
    i+=1


# In[ ]:


# Create a dataframe with a column called Tweets
df = pd.DataFrame([tweet.full_text for tweet in posts],columns =['Tweets'])

# Show the first 5 rows of data
df.head()


# In[ ]:


emoj = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002500-\U00002BEF"  # chinese char
        u"\U00002702-\U000027B0"
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U00010000-\U0010ffff"
        u"\u2640-\u2642" 
        u"\u2600-\u2B55"
        u"\u200d"
        u"\u23cf"
        u"\u23e9"
        u"\u231a"
        u"\ufe0f"  # dingbats
        u"\u3030"
                      "]+", re.UNICODE)


# In[ ]:


# Clean the text
# Create a function to clean the tweets
def cleanTxt(text):
    text = re.sub(r'@[A-Za-z0-9]+','', text) # Remove @mentions
    text = re.sub(r'#','',text) #Removing the '#' symbol
    text = re.sub(r'RT[\s]+','',text) # Removing RT
    text = re.sub(emoj,'',text)
    text = re.sub(r'NDTV','',text)
    text = re.sub(r'report+','',text)
    text = re.sub(r'!','',text)
    text = re.sub(r'\*','',text)
    text = re.sub(r'_','',text)
    text = re.sub(r'https:\/\/\S+','',text) # Remove the hyper link
    return text


# In[ ]:


# Clean the text
df['Tweets']=df['Tweets'].apply(cleanTxt)


# In[ ]:


# Show the cleaned text
df


# In[ ]:


#j=1
#for i in range(0,df.shape[0]):
#        print(str(j)+' ) '+ df['Tweets'][i])
#        print()
#        j+=1 


# In[ ]:


# Create a function to get the subjectivity
def getSubjectivity(text):
    return TextBlob(text).sentiment.subjectivity

# Create a function to get the polarity
def getPolarity(text):
    return TextBlob(text).sentiment.polarity


# In[ ]:


#Create two new columns
df['Subjectivity'] = df['Tweets'].apply(getSubjectivity)
df['Polarity'] = df['Tweets'].apply(getPolarity)


# In[ ]:


# Show the new dataframe with the new columns
df


# In[ ]:


# Plot The Word Cloud
allWords = ' '.join([twts for twts in df['Tweets']])
wordCloud = WordCloud(width = 500, height = 300, random_state = 21, max_font_size = 119).generate(allWords)
plt.imshow(wordCloud,interpolation = 'bilinear')
plt.axis('off')
plt.show()


# In[ ]:


# Create a function to compute the negitive, nutral and positive analysis
def getAnalysis(score):
    if score < 0:
        return 'Negative'
    elif score == 0:
        return 'Nutral'
    else:
        return 'Positive'


# In[ ]:


df['Analysis'] = df['Polarity'].apply(getAnalysis)
# Show the dataframe
df


# In[ ]:


# Print all of the postiive tweets
j=1
sortedDF = df.sort_values(by = ['Polarity'])
for i in range(0,sortedDF.shape[0]):
    if sortedDF['Analysis'][i] == 'Positive':
        print(str(j)+' ) '+ sortedDF['Tweets'][i])
        print()
        j+=1 


# In[ ]:


# Print all of the negative tweets
j=1
sortedDF = df.sort_values(by=['Polarity'],ascending =False)
for i in range(0,sortedDF.shape[0]):
    if sortedDF['Analysis'][i] == 'Negative':
        print(str(j)+' ) '+ sortedDF['Tweets'][i])
        print()
        j+=1 


# In[ ]:


# Plot the polarity and subjectivity
plt.figure(figsize = (8,6))
for i in range(0,df.shape[0]):
    plt.scatter(df['Polarity'][i],df['Subjectivity'][i], color = 'Blue')
plt.title('Sentiment Analysis')
plt.xlabel('Polarity')
plt.ylabel('Subjectivity')
plt.show()


# In[ ]:


# Get the percentage of positive tweets
ptweets = df[df.Analysis == 'Positive']
ptweets = ptweets['Tweets']

round((ptweets.shape[0]/df.shape[0])*100,1)


# In[ ]:


# Get the percentage of Negative tweets
ntweets = df[df.Analysis == 'Negative']
ntweets = ntweets['Tweets']

round((ntweets.shape[0]/df.shape[0])*100,1)


# In[ ]:


# Show the value counts
df['Analysis'].value_counts()

#plot and visualize the counts
plt.title('Sentiment Analysis')
plt.xlabel('Sentiment')
plt.ylabel('Counts')
df['Analysis'].value_counts().plot(kind='bar')
plt.show()


# In[ ]:





# In[ ]:




