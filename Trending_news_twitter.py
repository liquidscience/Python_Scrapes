#Author - Samaksh Yadav
#Description - "get_json_tweets" generate a rankking of trending nbews hashtags and then retrieves news,videos,reponses for the top 5 hastag trending in last 4 days'
#Version 1.1






def get_json_tweets():
    try:
            import datetime
            import tweepy
            import json
            from ttp import ttp
            import operator
            consumer_key = 'orVBG7irMKWuPZVzVMHmF'			#Intentionally truncated to prevent misuse
            consumer_secret = 'iuujp0hKDAYNkK60C7cn4z34lNyGiX686l2BvVtOA'	#Intentionally truncated to prevent misuse
            access_token = '986776236-0S9XqKSH5mtXq9o4IbSM6sVnDP63ifbUEKu'	#Intentionally truncated to prevent misuse
            access_token_secret = 'JkWIrlvCgpomr1hIcniAcxuOGuIw3xCDZmJcIq'	#Intentionally truncated to prevent misuse

            handle={}
            trend_setter={}


            def trend_search(hash_list):
                consumer_key = 'orVBG7irMKWuPZEjzVMHmF'	#Intentionally truncated to prevent misuse
                consumer_secret = 'iuujp0hKDAYNkKlNyGiX686l2BvVtOA'	#Intentionally truncated to prevent misuse
                access_token = '986776236-0S9XqKSH5mtVnDP63ifbUEKu'	#Intentionally truncated to prevent misuse
                access_token_secret = 'JkWIrlvCgpomr1hIcntGuIw3xCDZmJcIq'	#Intentionally truncated to prevent misuse
                auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
                auth.set_access_token(access_token, access_token_secret)
                api = tweepy.API(auth)
                json_response={}
                for hash in hash_list:
                    q=hash+" -RT"			#Remove results that are Retweets
                    print q
                    alltweets=api.search(q,count=5,result_type='recent')		#Search 5 recent tweets for specified hashtag
                    allvideos=api.search(hash,count=2,result_type='popular',filter="videos")	#Search 2 videos for specified hashtag
                    allnews=api.search(hash,count=3,result_type='news')		#Search 3 recent news for specified hashtag
                    list=[]
                    for news in allnews:
                        list.append(api.get_oembed(news.id))
                    for video in allvideos:
                        list.append(api.get_oembed(video.id))		#Get oembed code for easy embeding on front end for specified tweet
                    #print json.dumps(api.get_oembed(allnews[0].id))		
                    for tweets in alltweets:
                        list.append(api.get_oembed(tweets.id))

                    json_response[hash]=list

                return json.dumps(json_response)


            p = ttp.Parser()					#twitter-text-python library for parsing tweets

            def get_all_tweets(screen_name):


                alltweets = []
                auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
                auth.set_access_token(access_token, access_token_secret)
                api = tweepy.API(auth)





                new_tweets = api.user_timeline(screen_name = screen_name,count=200)
                alltweets.extend(new_tweets)
                oldest = alltweets[-1].id - 1

                while len(new_tweets) > 0:
                    try:
                        print(screen_name)
                        print "getting tweets before %s" % (oldest)
                        new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
                        alltweets.extend(new_tweets)
                        oldest = alltweets[-1].id - 1		#start from last retrived id

                        print "...%s tweets downloaded so far" % (len(alltweets))

                        if ( datetime.datetime.now().timetuple().tm_yday-alltweets[-1].created_at.timetuple().tm_yday)>4:	#Dont retrieve tweets more than 4 days old
                            break
                    except:
                        pass



                data=[]
                for tweet in alltweets:
                    if "#ICYMI" not in tweet.text:				#ICYMI 'IN CASE YOU MISSED IT' is generally not relevant to recent news result
                        if  len(p.parse(tweet.text).tags) :
                            url_list=[]
                            for url in tweet.entities['urls']:
                                if 'twitter' in url['expanded_url']:
                                    continue
                                url_list.append(url['expanded_url'])
                            data.append([tweet.created_at,(p.parse(tweet.text).tags),url_list,tweet.text])
                            

                cur_date=datetime.datetime.now()
                for d in data:
                    for hash in d[1]:
                        for url in d[2]:
                            
                            if hash not in handle:
                                handle[hash]=set()
                                handle[hash].add(screen_name)
                            else:
                                handle[hash].add(screen_name)


                            if hash not in trend_setter:			#new hashtag to add in list of hashes
                         
                                trend_setter[hash]=set()
                                trend_setter[hash].add((url,(cur_date-d[0]).total_seconds()//3600))  # url and hour elapsed for the current tweet
                            else :
                               
                                trend_setter[hash].add((url,(cur_date-d[0]).total_seconds()//3600))	 # url and hour elapsed for the current tweet
                            




               



            if __name__ == '__main__':
                 #pass in the username of the account you want to download
                print(datetime.datetime.now().second)
                get_all_tweets("ndtv")

                get_all_tweets("firstpost")
                get_all_tweets("htTweets")
                get_all_tweets("timesofindia")
                get_all_tweets('ibnlive')

                freq_dict={}
                for key, value in trend_setter.iteritems():
                    freq_dict[key]=len(value)



                ranking={}
                for key, value in trend_setter.iteritems():
                    if len(handle[key])>1:			#hashtag must  be mentioned in more than one handle ,to filter loacalized hashtags
                        sums=0.0
                        for tuple in value:
                            sums+=tuple[1]

                        ranking[key]=(1+0.0)/len(value)+(sums/len(value))/105			#Normalizing hashtag ranks based on no. of tweets and recentness of tweets


                sorted_x = sorted(ranking.items(), key=operator.itemgetter(1))

                data=[]
                for i,x in enumerate(sorted_x):
                    sorted_urls=sorted(trend_setter[x[0]],key=operator.itemgetter(1))
                    data.append([str(i+1),"#"+str(x[0]),str(x[1]),"   "+str(sorted_urls)])
					
					
				#"data" can be printed to see a list of hashtags and (news links,hour elapsed) combination for each hastag 	
					

                count=0
                send=[]
                for d in data:
                    if count<5:				#Search for tweets of top 5 hashtags
                        send.append(d[1])
                    else:
                        break;
                    count=count+1

                return trend_search(send)		#Search for tweets of top 5 hashtags
    except Exception as e:
        print e
        pass




json=get_json_tweets();
print json