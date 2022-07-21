import bs4
import requests

'''
response = requests.get('https://platzi.com')
soup = bs4.BeautifulSoup(response.text,'html.parser')
courses_links = soup.select('.Categories-category-item')
courses = [course['href'] for course in courses_links]

for course in courses:
  print(course)

'''
response = requests.get('https://www.elcomercio.pe')
soup = bs4.BeautifulSoup(response.text, 'html.parser')
links = soup.select('.fs-wi__title a')
tittles = [tittle['href'] for tittle in links]

for tittle in tittles:
    print(tittle)

print(soup.title.text)

print('\n')  
print(soup.select('meta[name=description]'))
print('\n')  
print(soup.select('meta[name=description]')[0]['lang']) 

#print(soup)



