import requests
from bs4 import BeautifulSoup
import sys

def get_rid_of_parentheses(test_str):
    ret = ''
    skip1c = 0
    skip2c = 0
    for i in test_str:
        if i == '(':
            skip2c += 1
        elif i == ')'and skip2c > 0:
            skip2c -= 1
        elif skip1c == 0 and skip2c == 0:
            ret += i
    return ret

def get_next(request):
    r = requests.get("https://en.wikipedia.org" + request)
    if r.status_code != 200:
        print('It leads to a dead end !')
        exit(1)
    soup = BeautifulSoup(r.text, 'html.parser')
    for div in soup.find_all(class_='hatnote'): 
        div.decompose()
    for div in soup.find_all('table'): 
        div.decompose()
    for div in soup.find_all(class_='thumb'): 
        div.decompose()
    cleansoupstr = get_rid_of_parentheses(str(soup))
    cleansoup = BeautifulSoup(cleansoupstr, 'html.parser')
    content = cleansoup.find_all(class_='mw-parser-output')
    if len(content) > 0:
        links = content[0].find_all('a')
        next_request = ''
        if len(links) > 0:
            for link in links:
                if (link.attrs.get("href") != None) and ((not '(disambiguation)' in link.attrs.get('href')) and (not ':' in link.attrs.get('href')) and ('/wiki/' in link.attrs.get('href'))):
                    next_request = link.attrs.get('href')
                    break
        if len(next_request) == 0:
            print('It leads to a dead end !')
            exit(1)
        return (next_request)
    else:
        print('It leads to a dead end !')
        exit(1)

def count_links(request):
    pages_seen = []
    pages_seen.append(request)
    count = 0
    while (not '/wiki/Philosophy' in pages_seen):
        if (len(pages_seen) == len(set(pages_seen))):
            count += 1
            print(pages_seen[-1].replace('/wiki/', '').replace('_', ' ')) # this line is to see each visited page as they come
            pages_seen.append(get_next(pages_seen[-1]))
        else:
            print('It leads to an infinite loop !')
            exit(1)
    print('{} roads from {} to philosophy !'.format(count, request.replace('/wiki/', '').replace('_', ' ')))

if __name__ == '__main__':
    if len(sys.argv) == 2:
        request = sys.argv[1]
        count_links('/wiki/' + request)
    else:
        print('specify query string please')