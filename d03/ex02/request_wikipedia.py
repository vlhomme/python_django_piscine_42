import requests
import dewiki
import sys, json

if __name__ == '__main__':
    if len(sys.argv) == 2:
        r = requests.get('https://en.wikipedia.org/w/api.php?action=query&prop=revisions&titles={0}&format=json&rvprop=content'.format(sys.argv[1]))
        if r.status_code != 200:
            print("Erreur HTTP, code ", str(r.status_code))
            exit(1)
        res = r.json()
        ok = ''
        if res.get('query'):
            if res['query'].get('pages'):
                pages = res['query']['pages']
                for pageId in pages:
                    if (pages[pageId].get('revisions')):
                        ok += pages[pageId]['revisions'][0]['*']
        else:
            print('search didn\'t found valid informations')
        if len(ok) > 0:
            f = open(sys.argv[1].replace(" ", "_") + '.wiki', "w")
            f.write(dewiki.from_string(ok))
            f.close()
    else:
        print('you must provide a query parameter as argument')

#https://en.wikipedia.org/w/api.php?action=query&prop=revisions&titles=chocolatine&format=json
#https://en.wikipedia.org/?curid=4685852