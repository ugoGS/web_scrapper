import requests
import bs4

#from IPython.display import Markdown, display_markdown

url = 'https://elcomercio.pe/'
#url = 'http://www.eluniversal.com.mx'

response = requests.get(url)
soup = bs4.BeautifulSoup(response.text, 'html.parser')

news = soup.select('.fs-wi__title a')
#news = soup.select('.titulo  a')

for new in news:
    print(new.text)
    print(url + new['href'])
    print('\n')


    #display_markdown(Markdown(f"### **Titulo: {new.text}** \n Enlace: {url + new['href']}"))