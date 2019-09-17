def rest_tweets(self, query, lang="pt", limit=None):
        """
        returns all the tweets within 7 days top according to the query received by this method
        returns the complete tweet
        :param query: should contain all the words and can include logic operators
        should also provide the period of time for the search
        ex: rock OR axe 
        (visit https://dev.twitter.com/rest/public/search to see how to create a query)
        :param lang: the language of the tweets
        :param limit: defines the maximum amount of tweets to fetch
        :return: tweets: a list of all tweets obtained after the request
        """
        tweets = []

        for tweet in tw.Cursor(self.api.search, q=query, lang=lang).items(limit):
            tweets.append(tweet._json)

        return tweets 
