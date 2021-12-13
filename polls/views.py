from django.http import HttpResponse
from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
import random
from django.views.decorators.csrf import csrf_exempt

def index(request):
    thoughts = []
    page = requests.get('https://www.inc.com/dave-kerpen/365-quotes-to-inspire-you-in-2014.html')
    soup = BeautifulSoup(page.content, 'lxml')
    ol = soup.find_all('ol')
    for ols in ol:
        li = ols.find('li')
        thought = li.text
        thoughts.append(thought)

    thoughtoftheday = (thoughts[random.randint(0,len(thoughts))])
    params = {"thought":thoughtoftheday}
    return render(request, "index.html", params)

def utility(request):
    return render(request, "utility.html")

@ csrf_exempt
def solution(request):
    userkaInp = request.POST.get("userinp", "User haven't entered anything yet.")
    userInp = request.POST.get("userinp", "")
    option = []
    answer = ""
    rempunc = request.POST.get("rempunc", "")
    remat = request.POST.get("remat","")    
    remnewline = request.POST.get("remnewline","")

    if rempunc == "on":
        option.append("Remove Punctuation")
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

        for char in userInp:
            if char not in (punctuations):
                    answer += char
        userInp = answer
        answer = ""

    if remat == "on":
        option.append("Remove '@'")
        for char in userInp:
            if char != '@':
                    answer += char
        userInp = answer
        answer = ""

    if remnewline == "on":
        option.append("Remove Newline")
        for char in userInp:
            if char != '\n' and char != '\r':
                    answer += char
        userInp = answer
        answer = ""

    strOption = ""
    strOption = strOption.join((", "+(i) for i in option))
    parameter = {"userkainput":userkaInp, "userkaselectkiyahuaoption":strOption[2:], "solution":userInp}
    return render(request, "solution.html", parameter)
