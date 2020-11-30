from django.shortcuts import render
from django.http import HttpResponse
# from django.template import Context, loader


# Create your views here.
    # template = loader.get_template("markdownCheatSheet")
def index(request):
    # return HttpResponse('<h1>ex00</h1>')
    return render(request, "markdownCheatSheet.html")