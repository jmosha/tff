

def getTimeline(self, limit=50000, resultType="recent"):
        try:
            tweets = []
            tweetsObj = tweepy.Cursor(self.API.home_timeline,
                    result_type=resultType,
                    exclude_replies = False).items(limit)
            
            pBar = tqdm(tweetsObj, ascii=True, total=limit, desc="Getting Tweets!")
            for cnt, tweet in enumerate(pBar):
                pBar.update(1)
                if not cnt < limit:
                    break
                tweets.append(tweet)
        except tweepy.error.TweepError as et:
            print(et)
        except Exception as e:
            print(e)
        return tweets 


