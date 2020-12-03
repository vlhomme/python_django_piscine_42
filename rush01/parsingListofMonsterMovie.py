import requests
from bs4 import BeautifulSoup
import sys
import json

def get_list(iteration):
    url = "https://www.senscritique.com/liste/Films_de_monstres/1124104#page-" + iteration +'/'
    print(url)
    r = requests.get(url)
    if r.status_code != 200:
        print('we broke it')
        exit(1)
    soup = BeautifulSoup(r.text, 'html.parser')
    whatWewantlist = soup.find_all(class_='elco-original-title')
    returnedList = []
    for element in whatWewantlist:
        returnedList.append(element.getText())
    return(returnedList)

def loopThroughPages():
    array = []
    for i in range (13):
        print(i)
        tmp = get_list(str(i + 1))
        # print(tmp)
        array = array + tmp
    with open('listOfTitles.json', "w", encoding="utf8") as outfile:
        # print(json.dumps(array))
        json.dump(array, outfile)

if __name__ == '__main__':
    loopThroughPages()