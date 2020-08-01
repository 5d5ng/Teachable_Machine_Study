# pluUrl에 저장해놓은 문자열을 naver에 검색해서 얻어낸 이미지파일 크롤링하는 코드

from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from urllib.parse import quote_plus
import os

baseUrl = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='
# plusUrl = input('검색어를 입력하세요 : ')
# plusUrl = ['송이버섯','표고버섯','양송이','새송이버섯','팽이버섯','느타리버섯','목이버섯','송로버섯','상황버섯','말굽버섯','송화버섯','방귀버섯'
#             ,'건버섯','구름버섯','잔나비걸상버섯','차가버섯','첸터럴버섯','돌버섯','대말불버섯']

plusUrl=['대말불버섯']# 한글 검색 자동 변환

n = 1
for imageName in plusUrl:
    url = baseUrl + quote_plus(imageName)
    html = urlopen(url)
    soup = bs(html, "html.parser")
    img = soup.find_all(class_='_img', limit=50)  # limit으로 다운받을 사진 제한 가능
    n = 1
    for i in img:
        imgUrl = i['data-source']
        with urlopen(imgUrl) as f:
            filename = './img/버섯/'+imageName + '/' + imageName + str(n)+'.jpg'
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            with open(filename, "wb") as h:  # w - write b - binary
                img = f.read()
                h.write(img)
        n += 1
    n =1
    print()
print('다운로드 완료')

# import os

# filename = "./br/baz.txt"
# os.makedirs(os.path.dirname(filename), exist_ok=True)
# with open(filename, "w") as f:
#     f.write("FOOBAR")
