import sys
import re
import os

def goForIt(file):
    try:
        with open('settings.py') as reader:
            arrayOfValues = []
            for line in reader:
                array = line.strip().split('=')
                i = 0
                for el in array:
                    if '"' in el:
                        array[i] = el.replace('"', '').strip()
                    else:
                        array[i] = el.strip()
                    i += 1
                arrayOfValues.append(array)
            print(arrayOfValues)
        f = open("template.html", "a")
        with open(file) as reader:
            for line in reader:
                myLine = line
                matched = re.findall("{(.*?)}", line)
                if len(matched) > 0:
                    for replace in arrayOfValues:
                        for word in matched:
                            if word == replace[0]:
                                myLine = myLine.replace('{' + word + "}", replace[1])
                    f.write(myLine)
                else:
                    f.write(line)
        f.close()
    except FileNotFoundError as e:
        print("file {} is not in directory".format(e.filename))
        sys.exit(0)
    except PermissionError as e:
        print("problem of read wrights on {}".format(e.filename))
        sys.exit(0)
    except Exception as e:
        print("error while opening".format(e))
        sys.exit(0)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        filename, fileExtension = os.path.splitext(sys.argv[1])
        if (fileExtension == ".template"):
            goForIt(sys.argv[1])