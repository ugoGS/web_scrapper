import logging
import shutil
from os import remove
from re import sub
logging.basicConfig(level=logging.INFO)
import subprocess

logger = logging.getLogger(__name__)
news_sites_uids = ['elpais'] #, 'elcomercio', 'eluniversal', 'lanacion']

def main():
    _extract()
    _transform()
    _load()

def _extract():
    for news_site_uid in news_sites_uids:
        logger.info('Starting extract process')
        subprocess.run(['py', 'main.py', news_site_uid], cwd='./extract')
        #s = r'C:\Users\Lenovo\web_scrapper\extract\elpais.csv'
        #d = r'C:\Users\Lenovo\web_scrapper\transform\elpais.csv'
        #shutil.move(s,d, copy_function=shutil.copy)
        shutil.move('extract\\{}.csv'.format(news_site_uid), 'transform\\{}.csv'.format(news_site_uid), copy_function=shutil.copy)
    '''
    for news_site_uid in news_sites_uids:
        subprocess.run(['py', 'main.py', news_site_uid], cwd='./extract')
        subprocess.run(['MOVE', '*.csv', '{}', '../transform/{}_.csv'.format(news_site_uid), ';'], cwd='./extract')])
        subprocess.run(['find', '.', '-name', '{}*'.format(news_site_uid), '-exec', 'mv', '{}', '../transform/{}_.csv'.format(news_site_uid), ';'], cwd='./extract')
    '''
def _transform():
    logger.info('Starting transform process')
    for news_site_uid in news_sites_uids:
        dirty_data_filename = '{}.csv'.format(news_site_uid)
        clean_data_filename = 'clean_{}'.format(dirty_data_filename)
        subprocess.run(['py', 'main.py', dirty_data_filename], cwd='./transform')
        remove('transform\\{}'.format(dirty_data_filename))
        shutil.move('transform\\{}'.format(clean_data_filename), 'load\\{}.csv'.format(news_site_uid), copy_function=shutil.copy)
        '''
        subprocess.run(['rm', dirty_data_filename], cwd='./transform')
        subprocess.run(['mv', clean_data_filename, '../load/{}.csv'.format(news_site_uid)], cwd='./transform')
        '''
def _load():
    logger.info('Starting loading process')
    for news_site_uid in news_sites_uids:
        clean_data_filename = '{}.csv'.format(news_site_uid)
        subprocess.run(['py', 'main.py', clean_data_filename], cwd='./load')
        remove('load\\{}'.format(clean_data_filename))

if __name__ == '__main__':
    main()