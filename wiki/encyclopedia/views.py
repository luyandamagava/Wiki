from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.urls import reverse
from random import randrange


from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def title(request):

    entries = util.list_entries()
    
    if request.method == "GET":
        query = request.GET["q"]

        subString = []
        for entry in entries:
            if query in entry:
                subString.append(entry)
                

        if query in entries:
            return render(request, "encyclopedia/title.html", {
                "text": util.get_entry(query),
                "query": query

            })
        
        
        
        else:
            if subString:
                return render(request, "encyclopedia/search.html",  {
                    "text": "Your search returned the current results",
                    "query": query,
                    "entries": subString
                    })
            
            else:
                return render(request, "encyclopedia/search.html",  {
                    "text": "No encylopedia entries matched the search you entered",
                    "query": query,
                    "entries": subString
                    })

        
def newPage(request):
    return render(request, "encyclopedia/newPage.html")
        

def titleLink(request, query):
    entries = util.list_entries()

    if query in entries:
        return render(request, "encyclopedia/title.html", {
            "text": util.get_entry(query),
            "query": query

        })

def newEntry(request):

    if request.method == "GET":
        EntryInfo = request.GET["EntryInfo"]
        EntryName = request.GET["EntryName"]

        util.save_entry(EntryName, EntryInfo)

        return render(request, "encyclopedia/title.html",{
            "text": util.get_entry(EntryName),
            "query": EntryName
        })
    
    else:
        return render(request, "encyclopedia/search.html", {
            "text": "Something went horribly wrong fam"
        })
        

def editPage(request, query):

    entry = util.get_entry(query)

    return render(request, "encyclopedia/editPage.html", {
        "query": query, 
        "text": entry
    })

def randomPage(request):

    entries = util.list_entries()

    num = randrange(len(entries))

    query = entries[num]

    text = util.get_entry(query)

    return render(request, "encyclopedia/title.html", {
        "text": text,
        "query": query,
    })




 


