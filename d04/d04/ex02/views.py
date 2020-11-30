from django.shortcuts import render
from datetime import datetime
import logging
import os
from ex02.forms import Myform

def extractLogs():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ffile = open(BASE_DIR + '/log/submit.log', 'r')
    data = ffile.readlines()
    goodList = []
    if ('Ex02Logyolo\n' in data):
        i = 0
        for line in data:
            if line == 'Ex02Logyolo\n':
                goodList.append(data[i + 1])
            i = i + 1
    ffile.close()
    return goodList


# Create your views here.
def index(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    initialStuff = extractLogs()
    if (request.method == 'POST'):
        form = Myform(request.POST)
        if form.is_valid():
            ffile = open(BASE_DIR + '/log/submit.log', 'a')
            text = form.cleaned_data['text']
            now = str(datetime.now())
            markupToFindLines = 'Ex02Logyolo\n'
            ffile.write(markupToFindLines)
            ffile.write(now + ', ' + text + '\n')
            ffile.close()
            okBoomer = extractLogs()
            newForm = Myform()
            return render(request, 'index.html', {'form' : newForm, 'okBoomer' : okBoomer})
    elif (len(initialStuff) > 0):
        # WE HAVE SOME LOGS
        form = Myform()
        return render(request, "index.html", {'form' : form, 'okBoomer' : initialStuff})
    else:
        form = Myform()
    return render(request, "index.html", {'form' : form})