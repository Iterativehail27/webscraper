from bs4 import BeautifulSoup
import requests


class Style:
    BOLD = '\033[1m'
    END = '\033[0m'


class HTML:
    cryptogazette = str('https://cryptogazette.com/all-articles/')
    cryptonews = str('https://cryptonews.com/news/')
    cryptocoinnews = str('https://cryptocoin.news/category/news/')
    cryptoknowmics = str('https://www.cryptoknowmics.com/news/cryptocurrency-news/')
    dailyhodl = str('https://dailyhodl.com/news/')


 #----Cryptogazette.com News----#


source = requests.get(HTML.cryptogazette).text
soup = BeautifulSoup(source, 'lxml')

CGheading = soup.find('div', 'article-inner-wrapper clearfix').a.span.text
CGlink = soup.find('div', 'article-inner-wrapper clearfix').a.get('href')
CGpicture = soup.find('div', 'article-inner-wrapper clearfix').img.get('src')
CGdate = soup.find('div', 'article-inner-wrapper clearfix').find('span', {'class':'meta-date'}).time.text

print()
print(Style.BOLD + '|Cryptogazette News|' + Style.END)
print(CGheading)
print(CGlink)
print(CGpicture)
print(CGdate)
print()

 #----Cryptonews.com News----#


source = requests.get(HTML.cryptonews).text
soup = BeautifulSoup(source, 'lxml')

CNheading = soup.find_all('div', {'class':'cn-tile article'})[0].h4.text
CNlink1 = soup.find_all('div', {'class':'cn-tile article'})[0].h4.a.get('href')
CNlink = 'https://cryptonews.com' + str(CNlink1)
CNpicture = soup.find_all('div', {'class':'cn-tile article'})[0].a.img.get('data-src')
CNdate = soup.find_all('div', {'class':'cn-tile article'})[0].i.text

print(Style.BOLD + '|Cryptonews News|' + Style.END)
print(CNheading)
print(CNlink)
print(CNpicture)
print(CNdate)
print()

 #----Cryptocoin.news News----#


source = requests.get(HTML.cryptocoinnews).text
soup = BeautifulSoup(source, 'lxml')

CCheading = soup.find_all('div', {'class':'td-module-thumb'})[0].a.get('title')
CClink = soup.find_all('div', {'class':'td-module-thumb'})[0].a.get('href')
CCpicture = soup.find('div', {'class':'td-module-thumb'}).a.img.get('src')
CCdate = soup.find('div', 'td-meta-info-container').time.text

print(Style.BOLD + '|Cryptocoin News|' + Style.END)
print(CCheading)
print(CClink)
print(CCpicture)
print(CCdate)
print()

 #----Cryptoknowmics.com News----#


source = requests.get(HTML.cryptoknowmics).text
soup = BeautifulSoup(source, 'lxml')

BBheading = soup.find('div', 'wrapper').h2.a.text
BBlink = soup.find('div', 'wrapper').h2.a.get('href')
BBpicture = soup.find('div', 'wrapper').find('div', {'class':'thumb entry-thumbnail video-thumb'}).img.get('src')
BBdate = soup.find('div', 'wrapper').small.text

print(Style.BOLD + '|Cryptoknowmics News|' + Style.END)
print(BBheading)
print(BBlink)
print(BBpicture)
print(BBdate)
print()

 #----Dailyhodl.com News----#


source = requests.get(HTML.dailyhodl).text
soup = BeautifulSoup(source, 'lxml')

DHheading = soup.find('article').h3.a.text
DHlink = soup.find('article').a.get('href')
DHpicture = soup.find('article').a.div.img.get('src')
DHdate = soup.find('article').find('div', {'class':'jeg_meta_date'}).text

print(Style.BOLD + '|Dailyhodl News|' + Style.END)
print(DHheading)
print(DHlink)
print(DHpicture)
print(DHdate)
print()
