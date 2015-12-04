#Author - Samaksh Yadav
#Description - The following scraper scrapes rencent content available at FIRSTPOST.COM
#Version 1.0




import feedparser

from urllib2 import urlopen
from bs4 import BeautifulSoup


rss={'http://www.firstpost.com/world/feed',
     'http://www.firstpost.com/economy/feed',
'http://www.firstpost.com/living/feed',
'http://www.firstpost.com/sports/feed',
'http://www.firstpost.com/india/feed',
'http://www.firstpost.com/politics/feed',
'http://www.firstpost.com/business/feed',
'http://www.firstpost.com/investing/feed',
'http://www.firstpost.com/bollywood/feed',
'http://www.firstpost.com/tech/feed',
'http://www.firstpost.com/travel/feed'
}


for key in rss:
  print(key)
  d = feedparser.parse(key)
  for post in d.entries:
    try:
      html=urlopen(post.link)
      bsObj=BeautifulSoup(html,"html.parser")
      title=post.title
      image= bsObj.find("meta",attrs={"property":"og:image"})["content"]
      description=bsObj.find("meta",attrs={"property":"og:description"})["content"]

      pubdate=bsObj.find("meta",attrs={"property":"article:published_time"})["content"]

      full_story=bsObj.find("div",attrs={"class":"fullCont1"}).get_text();

      print title
      print image
      print description
      print pubdate
      print full_story


      print "\n\n"
    except Exception as e:
        print e
        pass