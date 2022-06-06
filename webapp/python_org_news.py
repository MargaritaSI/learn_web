import requests
from bs4 import BeautifulSoup

def get_html(url):  # requesting html news data from site
    try:
        result = requests.get(url)
        result.raise_for_status()  # will handle exception + return value (won't receive a non-valid page from server with error)
        return result.text #
    except(requests.RequestException, ValueError): # network problem / after raise_for_status
        print('print network error')
        return False

def get_python_news(): # take html elements tree from -> html
    html = get_html('https://www.python.org/blogs/')  # our web page for searching
    if html:  # with open('python.org.html', 'w', encoding='utf=8') as f: # created python.org.html with data
        soup = BeautifulSoup(html, 'html.parser') # 'soup' accepts html and make a parser - 'soup' now converted html to html tree where we can search
        all_news = soup.find('ul', class_='list-recent-posts').findAll('li')  # searching not all 'ul' -only ul with class_='list-recent-post'
        #all_news=all_news.findAll('li')  # not all -only with 'li' and separate 'li' separately
        print(all_news)
        result_news = []
        for news in all_news:
            title = news.find('a').text # tied to a.text
            url = news.find('a')['href'] # tied to 'a'['href'] + call like to dictionary key
            published = news.find('time').text # tied to 'time' and call like to property
            result_news.append({  #  create list of dictionary
                'title': title,
                'url': url,
                'published': published
            })
        return result_news
    return False

