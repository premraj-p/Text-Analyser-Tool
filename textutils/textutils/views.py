#I have created this website

from django.http import HttpResponse   #write to avoid error
from django.shortcuts import render



def index(request):
    # params = {'name':'premraj' , 'place':'pune'}
    return render(request , 'index.html' )
                 #request , page name

   # return HttpResponse("Home")

def analyze(request):
    #get the text
    djtext=request.POST.get('text' , 'default')

    #checkbox value
    removepunc=request.POST.get('removepunc' , 'Off')
    uppercase=request.POST.get('uppercase' , 'Off')
    newlineremover=request.POST.get('newlineremover' , 'Off')
    spaceremover=request.POST.get('spaceremover' , 'Off')
    charcount=request.POST.get('charcount' , 'Off')

    #perform the functions one by one  if checkbox is on
    if removepunc=="on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        # analyzed = djtext
        params = {'purpose': 'Remove Puntuationns', 'analyzed_text': analyzed}
        djtext=analyzed
        # analyze the text
        # return render(request, 'analyze.html', params)

    if(uppercase=="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose': 'Change to uppercase', 'analyzed_text': analyzed}
        djtext=analyzed
        # analyze the text
        #return render(request, 'analyze.html', params)

    if(newlineremover=="on"):
        analyzed = ""
        for char in djtext:
            if char !="\n" and char!="\r":
              analyzed = analyzed + char
        params = {'purpose': 'Remove Newline', 'analyzed_text': analyzed}
        djtext=analyzed
        # analyze the text
        #return render(request, 'analyze.html', params)

    if(spaceremover=="on"):
        analyzed = ""
        for index,char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index + 1]==" "):
               analyzed=analyzed+char

        params = {'purpose': 'Extra Space Remover', 'analyzed_text': analyzed}
        djtext=analyzed
        # analyze the text
        #return render(request, 'analyze.html', params)

    if (charcount == "on"):
        analyzed = len(djtext)
        params = {'purpose': 'Count Characters', 'analyzed_text': analyzed}

        #return render(request, 'analyze.html', params)

    if(removepunc!="on" and newlineremover!="on" and spaceremover!="on" and uppercase!="on" and charcount!="on"):
        return HttpResponse("Please Select Any Operation And Try Again")






    return render(request,'analyze.html' , params)














# def capitalizefirst(request):
#     return HttpResponse("capitalizefirst")
#
# def newlineremove(request):
#     return HttpResponse("newlineremove")
#
# def spaceremover(request):
#     return HttpResponse("spaceremover")
#
# def charcounter(request):
#     return HttpResponse("charcounter")
#
