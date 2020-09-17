if __name__ == '__main__':
    d = {
	'Hendrix' : '1942',
	'Allman' : '1946',
	'King' : '1925',
	'Clapton' : '1945',
	'Johnson' : '1911',
	'Berry' : '1926',
	'Vaughan' : '1954',
	'Cooder' : '1947',
	'Page' : '1944',
	'Richards' : '1943',
	'Hammett' : '1962',
	'Cobain' : '1967',
	'Garcia' : '1942',
	'Beck' : '1944',
	'Santana' : '1947',
	'Ramone' : '1948',
	'White' : '1975',
	'Frusciante': '1970',
	'Thompson' : '1949',
	'Burton' : '1939',
	}
    # sort a dict by value : https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
    sortedByYear = sorted(d.items(), key=lambda bla: bla[1])

    # create a dic with key = year and value = list of artist sorted by ascii
    myDic = {}
    for element in sortedByYear:
        if element[1] in myDic:
            myDic[element[1]].append(element[0])
            myDic[element[1]].sort()
        else:
            myDic[element[1]] = [element[0]]
    # print each musicians line by line
    for element in myDic.items():
        if len(element[1]) > 1:
            for el in element[1]:
                print(el)
        else:
            print(element[1][0])