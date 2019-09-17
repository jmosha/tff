

def get_and_process_tweets(user="realdonaldtrump"):
    """
    A function that uses tweepy to download all the tweets by a given `user`,
    processes the tweets for stopwords & weird internet formatting,
    tokenizes the tweets using the NLTK, and then uses markovify to output a
    reusable JSON file for use in generating future tweets.
    """

    all_tweets = []  # a list in which to store DJT's tweets.

    #get DJT's tweets.
    for tweet in tweepy.Cursor(api.user_timeline, id=user).items():
        if tweet.source == 'Twitter for Android':  # only get tweets from DJT's
                                                   # insecure Android phone
            fishy_tweet = clean_tweet(tweet.text)  # and add them to the list.
            all_tweets.append(fishy_tweet)

    # write his crappy tweets to a text file.
    with open('djt_tweets.txt', 'w') as f:
        for tweet in all_tweets:
            f.write(tweet + ' ')  # need the space so they don't stick together.

    # open the file to POS tag it and process the results into JSON.
    with open("djt_tweets.txt") as t:
            text = t.read()
    #
    text_model = POSifiedText(input_text=text, state_size=3)
    model_json = text_model.to_json()

    # save the json to disk for future use.
    with open('djt_tweets.json', 'w', encoding='utf-8') as j:
        json.dump(model_json, j, ensure_ascii=False) 


