import argparse 
import csv
import datetime
import logging
logging.basicConfig(level=logging.INFO)
import re

from requests.exceptions import HTTPError
from urllib3.exceptions import MaxRetryError

#Para referenciar a la clase NewsPage
import news_page_object as news

#config: Variable global que almacena el contenido de "yaml"
from common import config

#is_well_formed_url = re.compile(r'^https?://.+/$')
is_well_formed_url = re.compile(r'^https?://.+/.+$')
is_root_path = re.compile(r'^/.+$')

logger = logging.getLogger(__name__)

def _news_scrapper(news_site_uid): 
#Ej. news_site_uid -> elcomercio

    host = config()['news_sites'][news_site_uid]['url']
    #Ej. host -> http://www.elcomercio.pe

    logging.info('Beginning scrapper for {}'.format(host))
    logging.info('Finding links in homepage... ')

    homepage = news.HomePage(news_site_uid, host)

    '''
    # Imprimir links
    for link in homepage.article_links:   
        if is_well_formed_url.match(link):
            print(1)
            print(link)
        elif is_root_path.match(link):
            print(2)
            print('{host}{uri}'.format(host=host, uri=link))
        else:
            print(3) 
            print('{host}/{uri}'.format(host=host, uri=link))  
    '''

    articles = []
    for link in homepage.article_links:
        article = _fetch_article(news_site_uid, host, link)

        if article: 
            logger.info('Article fetched!')
            articles.append(article)

    _save_articles(news_site_uid, articles)
    
def _save_articles(news_site_uid, articles):
    now = datetime.datetime.now().strftime('%Y_%m_%d')
    '''
    out_file_name = '{news_site_uid}_{datetime}_articles.csv'.format(
        news_site_uid = news_site_uid,
        datetime = now)
    '''
    out_file_name = '{news_site_uid}.csv'.format(
        news_site_uid = news_site_uid)   
    csv_headers = list(filter(lambda property: not property.startswith('_'), 
    dir(articles[0])))
    
    with open(out_file_name, mode='w+') as f:
        writer = csv.writer(f)
        writer.writerow(csv_headers)

        for article in articles:
            try:
                row = [str(getattr(article, prop)) for prop in csv_headers]
                writer.writerow(row)
            except (UnicodeEncodeError) as e:
                logger.warning('charmap codec cant encode character u2033')

def _fetch_article(news_site_uid, host, link):
    logger.info('Start fetching article at {}'.format(_build_link(host,link)))

    article = None
    try:
        article = news.ArticlePage(news_site_uid, _build_link(host,link))
    except (HTTPError, MaxRetryError) as e:
        logger.warning('Error while fetching article!', exc_info=False)
    
    if article and not article.body:
        logger.warning('Invalid article. There is no body.')
        return None

    return article

def _build_link(host, link):
    if is_well_formed_url.match(link):
        return link
    elif is_root_path.match(link):
        return '{host}{uri}'.format(host=host, uri=link)
    else:
        return '{host}/{uri}'.format(host=host, uri=link)    
    
    '''   
    elif is_root_path(link):
        return '{}{}'.format(host, link)
    else:
        return '{}/{}'.format(host, link)
    '''  


if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    news_site_choices = list(config()['news_sites'].keys())
    parser.add_argument(
        'news_site',
        help='The news site that you want to scrape',
        type=str,
        choices=news_site_choices
    )

    args = parser.parse_args()
    _news_scrapper(args.news_site)



'''
    #Para visualizar la estructura 

    #Recorrer y mostrar diccionario de diccionarios:
    print('\n')
    for key, val in config().items():
        print('Llave: ' + key + ' Valor: ' + str(val))

        #Para recorrer y mostrar el diccionario de cada valor del diccionario anterior
        print('\n')
        for keyj, valj in val.items():
            print('Llave: ' + keyj + ' Valor: ' + str(valj))

            #Para recorrer y mostrar el diccionario de cada valor del diccionario anterior
            print('\n')
            for keyk, valk in valj.items():
                print('Llave: ' + keyk + ' Valor: ' + str(valk))

    print('\n')
    print('Diccionario completo:')
    print(config())
'''