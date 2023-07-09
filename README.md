# Sentiment Analysis on twittes of User
In this project, I have extracted real time data from twitter by creating secured channel which is in backend of code {sensitive information: configs, Twitter API credentials}.
Created a dataframe of tweets. 
Performed cleaning to remove: 
    **emoticons** with a generalized structure (symbols & pictographs, transport & map symbols, flags (iOS), chinese char)
    **@mentions, '#' symbol,  RT (Retwitted), hyper link, '!','*','_'**
    Some special cleaning line **'NDTV'**, **'report'** specially for twitter handler **screen_name = "ndtv"**.

Data Analysis on Dataframe of tweets on below critera: 

1. **Subjectivity**: relevency of content on scale of (0-1) 

2. **Polarity**: Classified the content Positive, Neutral, Negitive on scale reprasentation (1 to 0 to (-1)) respectively. 

3. Ploted The Word Cloud to drill down hot topics (size of world represent the repetion of a perticular word).

Based upon my study, 

1. Majorty of tweets have high subjectivity.

![image](https://github.com/Soni-Tush/Tushal_Soni/assets/109894934/aef3340d-11d8-48fc-abfb-3f6e402aa664)

2. 24.0 % of Tweets posted on "NDTV" tweeter account are impacting positively.

3. 15.5 % of Tweets are having harsh vocablary and thus having negitive polarity. 

![image](https://github.com/Soni-Tush/Tushal_Soni/assets/109894934/45c63e63-96d3-4fb3-9096-69ee754dc759)

4.  Hot topics posted during mid of Jan 2023 are having following words: 

![image](https://github.com/Soni-Tush/Tushal_Soni/assets/109894934/b4f74b2a-54f4-428f-b23e-b6ce563bab85) .


**Thank you for your time to go through my project on Sentiment Analysis hope it was helpful for you.**
