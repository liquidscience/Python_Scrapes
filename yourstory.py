#Author - Samaksh Yadav
#Description - The following scraper scrapes rencent content available at YOURSTORY.COM
#Version 1.0



from urllib2 import urlopen
from bs4 import BeautifulSoup



html = urlopen('http://yourstory.com/ys-stories/')
bsObj1 = BeautifulSoup(html,"html.parser")
resultset= bsObj1.findAll("a",attrs={"class":"block"})
imageset=bsObj1.findAll("div",attrs={"class":"imgWrapper block"})


i=0;
for result in resultset:
    try:
        image=imageset[i].findChildren()[0]["src"]

        i+=1
        html = urlopen(result['href'])
        bsObj = BeautifulSoup(html,"html.parser")
        description=bsObj.find("meta",attrs={"name":"description"})["content"]
        date=bsObj.find("meta",attrs={"property":"article:published_time"})["content"]

        title= bsObj.find("h3",attrs={"class":"title color-ys"}).text.strip()

        full_story= str(bsObj.find("div",attrs={"class":"ys_post_content text"})).decode('utf-8')

        simple_text=  bsObj.find("div",attrs={"class":"ys_post_content text"}).get_text()

        category= "yourstory"
        print title
        print image
        print description
        print full_story
        print simple_text
        print category
        print date



        print("\n\n\n\n\n\n")
    except Exception as e:
        print(e)