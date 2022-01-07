import requests
from bs4 import BeautifulSoup


#1 Indonesian Ecommerce
class Tokopedia:
    def __init__(self,query,lowest=True):
        self.query = query # search query
        self.lowest = lowest # sort by price is asc or desc in search query
        self.HEADERS = {
            'origin': 'https://www.tokopedia.com',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9',
            'accept': 'application/json, text/plain, */*',
            'referer': 'https://www.tokopedia.com/',
            'authority': 'ace.tokopedia.com',
            "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36 OPR/58.0.3135.79",
        }
    def fetch(self):
        if self.lowest:
            #ob (ordered by) : 3 -> price from low to high
            self.ob = 3
        else:
            #ob (ordered by) : 4 -> price from high to low
            self.ob = 4
        self.url = f"https://tokopedia.com/search?q={self.query}&st=product&ob={self.ob}"
        req = requests.get(self.url,headers=self.HEADERS)
        if req.status_code == 200:
            #this is a block code that do scrape things (extract the html data)
            soup = BeautifulSoup(req.text,"html.parser")
            prod = soup.find_all("div",{"class":"css-y5gcsw"})
            raw_data = []
            for x in prod:
                name = x.find("div",{"class":"css-12fc2sy"})
                price = x.find("div",{"class":"css-a94u6c"})
                stars = x.find("span",{"class":"css-1ffszw6"})
                seller = x.find_all("span",{"class":"css-qjiozs"})
                try:
                    fin = {
                        #"name" : "Logitech MX Master 3 Wireless Bluetooth Mouse MX Master3 - Graphite",
                        #"price" : "Rp1.299.000",
                        #"stars" : "4.9",
                        #"seller" : "",
                        #""
                    }
                    if name:
                        fin["name"] = name.string
                    else:
                        #assuming if product name is not found mean no relevant info to show
                        continue
                    if price:
                        fin["price"] = int(price.string.replace("Rp",""))
                    else:
                        fin["price"] = None
                    if stars:
                        fin["stars"] = stars.string
                    else:
                        fin["stars"] = None
                    if seller:
                        fin["seller"] = seller[1].string
                    else:
                        fin["seller"] = None
                    
                    #Additional Info
                    fin["souce"] = "Tokopedia"
                    raw_data.append(fin)
                except Exception as exc:
                    print(exc)
            #end of scrape block

            return raw_data
        else:
            return False
class Shoppee:
    pass

class Lazada:
    pass

class Bukalapak:
    pass

class Blibli:
    pass