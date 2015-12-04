#Author - Samaksh Yadav
#Description - The following scraper scrapes rencent content available at hindustantimes.com
#Version 1.0




from urllib2 import urlopen
from bs4 import BeautifulSoup

urls={
'http://www.hindustantimes.com/movie-reviews/top-news':'Reviews',
'http://www.hindustantimes.com/bollywood/top-news':'bollywood',
'http://www.hindustantimes.com/hollywood/top-news':'hollywood',
'http://www.hindustantimes.com/india/top-news':'india',
'http://www.hindustantimes.com/world/top-news':'world',
'http://www.hindustantimes.com/world-cinema/top-news':'world-cinema',
'http://www.hindustantimes.com/tv/top-news':'television',
'http://www.hindustantimes.com/music/top-news':'music',
'http://www.hindustantimes.com/sex-and-relationships/top-news':'sex-and-relationships',
'http://www.hindustantimes.com/fashion-and-trends/top-news':'fashion-and-trends',
'http://www.hindustantimes.com/art-and-culture/top-news':'art-and-culture',
'http://www.hindustantimes.com/travel/top-news':'travel',
'http://www.hindustantimes.com/books/top-news':'books',
'http://www.hindustantimes.com/tech-reviews/top-news':'tech-reviews',
'http://www.hindustantimes.com/gadgets/top-news':'gadgets',
'http://www.hindustantimes.com/apps/top-news':'apps',
'http://www.hindustantimes.com/social-media/top-news':'social-media',
'http://www.hindustantimes.com/education/top-news':'education',
'http://www.hindustantimes.com/business/top-news':'business',
'http://www.hindustantimes.com/real-estate/top-news':'real-estate',
'http://www.hindustantimes.com/autos/top-news':'autos',
'http://www.hindustantimes.com/opinion/top-news':'opinion'
}


for url,cat in urls.iteritems():
    html=urlopen(url)
    bsObj=BeautifulSoup(html,"html.parser")
    resultset=bsObj.find("div",attrs={"class":"search_pg_bg"}).findAll("li")

    try:
        for result in resultset:
            image= result.find("img")["src"]
            title= result.find("img")["alt"]
            description= result.find("div",attrs={"class":"web-summary"}).get_text()
            link= result.find("a")["href"]
            html1=urlopen(link)
            bsObj=BeautifulSoup(html1,"html.parser")
            story_list=bsObj.find("div",attrs={"class":"sty_txt"}).findAll("p")
            full_story=""
            for story in story_list:
                full_story+=story.get_text()+"\n"
            print title
            print image
            print description
            print link
            print full_story
            print cat
            print "\n\n"
    except Exception as e:
        print e
        pass

