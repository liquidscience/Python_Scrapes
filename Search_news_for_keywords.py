#Author - Saamaksh Yadav
#Description - Send any keyword to "search_to_json" to generate a json object of relevant news for the specified keyword
#Version 1.0





def search_to_json(search):
    from urllib2 import urlopen
    from bs4 import BeautifulSoup
    import json
    url_base='http://aninews.in/newsdetail/keyword-search/'
    search_str=search.replace(' ','-')
    url_end='.html'
    url= url_base+search_str+url_end

    html= urlopen(url)
    bsObj=BeautifulSoup(html,"html.parser")
    resultset=bsObj.findAll("div",attrs={"class":"catnewsbox"})
    list=[]
    for result in resultset:
        url=result.find("a")["href"]
        html= urlopen(url)
        bsObj=BeautifulSoup(html,"html.parser")
        image=bsObj.find("meta",attrs={"property":"og:image"})["content"]
        title=bsObj.find("meta",attrs={"property":"og:title"})["content"]
        story=bsObj.find("span",attrs={"style":"text-align:left;"}).get_text()
        description=bsObj.find("meta",attrs={"name":"description"})["content"]
        print title
        print image
        print description
        print story

        list.append({"title":title,"image":image,"description":description,"story":story})
        print "/n/n"
    return json.dumps(list)


print search_to_json("shah rukh khan")