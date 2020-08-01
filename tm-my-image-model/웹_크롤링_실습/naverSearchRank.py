import requests 
from bs4 import BeautifulSoup 
from urllib.request import urlopen 
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'} 
url = 'https://datalab.naver.com/keyword/realtimeList.naver?where=main' 
res = requests.get(url, headers = headers) 
soup = BeautifulSoup(res.content, 'html.parser') 
data = soup.select('span.item_title') 
i = 1
f = open("./검색순위.txt",'w',encoding="utf8")
for item in data:
  print(str(i)+"위 : " + item.get_text())
  data = str(i)+"위 : " + item.get_text()+"\n"
  f.write(data)
  i+=1
f.close()

# f = open("/Users/deo/Desktop/GitRepository/Handsome-Tomato/tm-my-image-model/수익형웹,앱")
# for i in range(1,11):
#   data = "{}번째 줄입니다.\n".format(i)
#   f.write(data)
# f.close()


