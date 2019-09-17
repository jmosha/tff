def get_tweets(listOfTweets, keyword, numOfTweets):
    # Iterate through all tweets containing the given word, api search mode
    for tweet in tweepy.Cursor(api.search, q=keyword).items(numOfTweets):
        # Add tweets in this format
        dict_ = {'Screen Name': tweet.user.screen_name,
                'User Name': tweet.user.name,
                'Tweet Created At': unicode(tweet.created_at),
                'Tweet Text': tweet.text,
                'User Location': unicode(tweet.user.location),
                'Tweet Coordinates': unicode(tweet.coordinates),
                'Retweet Count': unicode(tweet.retweet_count),
                'Retweeted': unicode(tweet.retweeted),
                'Phone Type': unicode(tweet.source),
                'Favorite Count': unicode(tweet.favorite_count),
                'Favorited': unicode(tweet.favorited),
                'Replied': unicode(tweet.in_reply_to_status_id_str)
                }
        listOfTweets.append(dict_)   
    return listOfTweets

# Connect to DB 
