def getItOut(numb, arra):
    return arra[numb].split(':')[1].strip()

def strToDic(string):
    name = string.split('=')[0].strip()
    rest = string.split('=')[1].strip().split(',')
    position = getItOut(0, rest)
    number = getItOut(1, rest)
    small = getItOut(2, rest)
    molar = getItOut(3, rest)
    electron = getItOut(4, rest)
    return ({
        "name": name,
        "position": position,
        "number": number,
        "small": small,
        "molar": molar,
        "electron": electron
    })

def read_it_and_return_a_pars():
    with open("periodic_table.txt") as f:
        bigList = []
        for line in f:
            element = strToDic(line)
            bigList.append(element)
    return(bigList)

def createTab(f, dic):
    cur = 0
    prev = 0
    htmlString = "<table>"
    for element in dic:
        cur = int(element['position'])
        if cur == 0:
            htmlString += "<tr>"
        if cur - prev > 1:
            htmlString += "<td colspan='" + str(cur - prev - 1) + "'></td>"
        htmlString += "<td><h4>" + element['name'] + "</h4>"
        htmlString += "<ul><li>" + element['number'] +"</li><li>" + element['small'] +"</li><li>" + element['molar'] + "</li></ul></td>"
        if cur == 17:
            htmlString += "</tr>"
            cur = 0
        prev = cur
    htmlString += "</table>"	
    f.write(htmlString)

def makeMeHtml(dic):
    with open("periodic_table.html", 'w') as f:
        f.write("<!DOCTYPE html>\n")
        f.write("<html lang='en'>\n")
        f.write("<head>\n<meta charset='UTF-8'><meta name='viewport' content='width=device-width, initial-scale=1.0'><title>Periodic table</title>\n")
        f.write("<style>table {	width: 90%;} td {border: 1px solid green; padding:5px} </style></head>\n")
        f.write("<body>\n")
        createTab(f, dic)
        f.write("</body>\n")
        f.write("</html>\n")

def just_make_it():
    dic = read_it_and_return_a_pars()
    makeMeHtml(dic)

if __name__ == '__main__':
    just_make_it()