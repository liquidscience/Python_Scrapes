#Author - Samaksh Yadav
#Description - The following scraper scrapes rencent content available at THELOGICALINDIAN.COM
#Version 1.0


import urllib2
import re
import json
from bs4 import BeautifulSoup
def open(str):
    req = urllib2.Request(str, headers={ 'User-Agent': 'Mozilla/5.0' })
    html = urllib2.urlopen(req).read()
    return html

urls=['http://thelogicalindian.com/category/story-feed/opinion/','http://thelogicalindian.com/category/story-feed/get-inspired/','http://thelogicalindian.com/category/story-feed/awareness/']
for url in urls:
    html = open(url)
    bsObj = BeautifulSoup(html,"html.parser")
    resultset= bsObj.findAll("h3",attrs={"class":"entry-title"})


    for result in resultset:
        try:
            title=result.text
            match = re.search(r'href=[\'"]?([^\'" >]+)', str(result))
            if match:
                html = open(str(match.group(0))[6:])
                bsObj = BeautifulSoup(html,"html.parser")
                description=bsObj.find("meta",attrs={"property":"og:description"})["content"]
                date=bsObj.find("meta",attrs={"property":"article:published_time"})["content"]


                simpletext=bsObj.find("div",attrs={"class":"entry-content clearfix"}).get_text()

                if(("Video" in simpletext or "video" in simpletext or "Watch" in simpletext or "watch" in simpletext)):
                     continue
                if(("Video" in title or "video" in title or "Watch" in title or "watch" in title)):
                     continue

                str1= str(bsObj.find("div",attrs={"class":"entry-content clearfix"})).decode('utf-8').replace("//thelogical","http://www.thelogical")



                pos=str1.find("<button")

                story_html=""
                 #story html
                if "Also Read" in str1[0:pos]:
                    pos1=str1[0:pos].find("Also Read")
                    story_html=str1[0:pos1]+"</strong></p></div> </div>"
                else:
                    story_html=str1[0:pos]+" </div> </div>"
                image=str(bsObj.find("meta",attrs={"name":"twitter:image"})['content'])
                category="logicalindian"

                print title
                print image
                print story_html
                print simpletext
                print date
                print description
                print category



                print("\n\n\n\n\n\n")
        except Exception as e:
            print e





