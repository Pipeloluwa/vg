# Create your views here.
from django.http import HttpResponse

from .models import Audio,Video,Artiste
from django.shortcuts import render, redirect
import random




global r1,r2,once
r1 = []
r2 = []
once = 0

global stp,lim,numb
stp=0
lim=0
numb=1


global no
no = 0

global former
former= None
global keeprow #for the audio page
global keeprow2 #for the audio page
global keeprow3 #for the audio page
keeprow,keeprow2,keeprow3= [],[],[]




def index(request):
    global former
    former=None
    if request.method=="POST":
        try:
            tok=request.POST.get("s_result")
            cont = Audio.objects.all()
            tok = tok.upper()
            got2 = []
            for i in cont:
                toU = str(i.title)
                if tok == toU.upper():
                    got2.append(i.identification_code)
            print(got2)
            return render(request, "search_course11.html", {"tok": tok, "got": cont, "got2": got2})
        except:
            return render(request, "search_course11.html", {"tok": None, "cont": None, "ck": False})


    else:
        sm = []
        nocr = 0
        lgic = len(Audio.objects.all())
        for i in range (lgic):
            if nocr==7:
                break
            rd=random.choice(Audio.objects.all())
            if nocr==0:
                sm.append(rd)
                nocr += 1
            if nocr!=0:
                if rd not in sm:
                    sm.append(rd)
                    nocr += 1
                else:
                    lgic+=1

        if sm:
            return render(request, "index1.html", {"sm":sm, "ca":True})
        return render(request, "index1.html", {"sm":sm, "ca":False})



def error404(request, exception):
    data= {}
    return render(request, "404.html", data)





def npage(request,nmbr):
    global keeprow
    nmbr+=1
    return render(request, "audio.html", {"enablepage": True, "nmbr": nmbr, "keeprow": keeprow[nmbr],"pageno":len(keeprow),
                                          "curr_page":nmbr+1})


def ppage(request,nmbr):
    global keeprow
    nmbr-=1
    return render(request, "audio.html", {"enablepage": True, "nmbr": nmbr, "keeprow": keeprow[nmbr],"pageno":len(keeprow),
                                          "curr_page":nmbr+1})


def vnpage(request,nmbr):
    global keeprow2
    nmbr+=1
    return render(request, "video.html", {"enablepage": True, "nmbr": nmbr, "keeprow": keeprow2[nmbr],"pageno":len(keeprow2),
                                          "curr_page":nmbr+1})

def vppage(request,nmbr):
    global keeprow2
    nmbr-=1
    return render(request, "video.html", {"enablepage": True, "nmbr": nmbr, "keeprow": keeprow2[nmbr],"pageno":len(keeprow2),
                                      "curr_page":nmbr+1})



def anpage(request,nmbr):
    global keeprow3
    nmbr+=1
    return render(request, "artist.html", {"enablepage": True, "nmbr": nmbr, "keeprow": keeprow3[nmbr],"pageno":len(keeprow3),
                                      "curr_page":nmbr+1})

def appage(request,nmbr):
    global keeprow3
    nmbr-=1
    return render(request, "artist.html", {"enablepage": True, "nmbr": nmbr, "keeprow": keeprow3[nmbr],"pageno":len(keeprow3),
                                      "curr_page":nmbr+1})



def about(request):
        return render(request, "about-2.html")

def recording(request):
        return render(request, "recording.html")

def home_recording(request):
        return render(request, "homerecording.html")

def rehearsal(request):
        return render(request, "rehearsal.html")

def mini(request):
        return render(request, "minisoundset.html")

def half(request):
        return render(request, "halfsoundset.html")

def full(request):
        return render(request, "fullsoundset.html")

def mega(request):
        return render(request, "megasoundset.html")

def music(request):
        return render(request, "musicschool.html")

def news(request):
        return render(request, "newsandarticles.html")


def audio(request):
    if request.method=="POST":
        nametok=request.POST.get("dzName")
        tok = nametok
        cont = Audio.objects.all()
        tok = tok.upper()
        got2 = None
        try:
            got2 = []
            for i in cont:
                toU = str(i.title)
                if tok == toU.upper():
                    got2.append(i.identification_code)
            return render(request, "search_course11.html", {"tok": tok, "got": cont, "got2": got2})
        except:
            return render(request, "search_course11.html", {"tok": tok, "cont": cont, "ck": False})

    else:
        global keeprow
        keeprow = []
        all_c = Audio.objects.all()
        keepobj=[]
        keepno=0
        nmbr=0
        for i in all_c:
            keepno+=1
            keepobj.append(i)
            if keepno==9:
                keepno=0
                keeprow.append(keepobj)
                keepobj = []

        if keepno != 0:#(1)if there is second row but its not up to 9 fields add the remaining fields OR (2)add keepobj because we only have one page only and it's not up to 9 fields
            keeprow.append(keepobj)
        if len(keeprow)> 1: #to enable page
            return render(request, "audio.html", {"enablepage": True, "nmbr": nmbr,"curr_page":nmbr+1,
                                "pageno":len(keeprow),"keeprow":keeprow[0]})
        return render(request, "audio.html",{"enablepage": False, "nmbr": nmbr, "keeprow": keeprow[0],
                                             "curr_page":nmbr+1})





def video(request):
    if request.method == "POST":
        nametok = request.POST.get("dzName")
        print("It is a Post: ", nametok)
        tok = nametok
        cont = Video.objects.all()
        tok = tok.upper()
        got2 = None
        try:
            got2 = []
            for i in cont:
                toU = str(i.title)
                if tok == toU.upper():
                    got2.append(i.identification_code)
            print(got2)
            return render(request, "search_course111.html", {"tok": tok, "got": cont, "got2": got2})
        except:
            return render(request, "search_course111.html", {"tok": tok, "cont": cont, "ck": False})
    else:
        global keeprow2
        keeprow2 = []
        all_c = Video.objects.all()
        keepobj = []
        keepno = 0
        nmbr = 0
        for i in all_c:
            keepno += 1
            keepobj.append(i)
            if keepno == 9:
                keepno = 0
                keeprow2.append(keepobj)
                keepobj = []

        if keepno != 0:  # (1)if there is second row but its not up to 9 fields add the remaining fields OR (2)add keepobj because we only have one page only and it's not up to 9 fields
            keeprow2.append(keepobj)
        if len(keeprow2) > 1:  # to enable page
            return render(request, "video.html", {"enablepage": True, "nmbr": nmbr, "curr_page": nmbr + 1,
                                                  "pageno": len(keeprow2), "keeprow": keeprow2[0]})
        return render(request, "video.html",
                      {"enablepage": False, "nmbr": nmbr, "keeprow": keeprow2[0],
                       "curr_page": nmbr + 1})



def artiste(request):
    if request.method == "POST":
        nametok = request.POST.get("dzName")
        print("It is a Post: ", nametok)
        tok = nametok
        cont = Artiste.objects.all()
        tok = tok.upper()
        got2 = None
        try:
            got2 = []
            for i in cont:
                toU = str(i.artiste)
                if tok == toU.upper():
                    got2.append(i.identification_code)
            print(got2)
            return render(request, "search_course1111.html", {"tok": tok, "got": cont, "got2": got2})
        except:
            return render(request, "search_course1111.html", {"tok": tok, "cont": cont, "ck": False})
    else:
        global keeprow3
        keeprow3 = []
        all_c = Artiste.objects.all()
        keepobj = []
        keepno = 0
        nmbr = 0
        for i in all_c:
            keepno += 1
            keepobj.append(i)
            if keepno == 9:
                keepno = 0
                keeprow3.append(keepobj)
                keepobj = []

        if keepno != 0:  # (1)if there is second row but its not up to 9 fields add the remaining fields OR (2)add keepobj because we only have one page only and it's not up to 9 fields
            keeprow3.append(keepobj)
        if len(keeprow3) > 1:  # to enable page
            return render(request, "artist.html", {"enablepage": True, "nmbr": nmbr, "curr_page": nmbr + 1,
                                                  "pageno": len(keeprow3), "keeprow": keeprow3[0],})
        return render(request, "artist.html",
                      {"enablepage": False, "nmbr": nmbr, "keeprow": keeprow3[0],
                       "curr_page": nmbr + 1})




def contact(request):
        return render(request, "contact-1.html")


def search_course1111(request, tok):
    try:
        if request.method == "POST":
            tok = request.POST.get("qq")
            cont = Artiste.objects.all()
            tok = tok.upper()
            got2 = None
            try:
                got2 = []
                for i in cont:
                    toU = str(i.title)
                    if tok == toU.upper():
                        got2.append(i.identification_code)
                print(got2)
                return render(request, "search_course1111.html", {"tok": tok, "got": cont, "got2": got2})

            except:
                return render(request, "search_course1111.html", {"tok": tok, "cont": cont, "ck": False})
        else:
            cont = Artiste.objects.all()
            try:
                got = Artiste.objects.get(identification_code=tok)
                return render(request, "search_course1111.html", {"tok": tok, "got": got, "ck": True})
            except:
                return render(request, "search_course1111.html", {"tok": tok, "cont": cont, "ck": False})
    except:
        try:
            tok = None
            return render(request, "search_course1111.html", {"tok": tok, "cont": cont, "ck": False})
        except:
            return HttpResponse("Your Search input was Empty")

def search_course111(request, tok):
    try:
        if request.method == "POST":
            tok = request.POST.get("qq")
            cont = Video.objects.all()
            tok = tok.upper()
            got2 = None
            try:
                got2 = []
                for i in cont:
                    toU = str(i.title)
                    if tok == toU.upper():
                        got2.append(i.identification_code)
                print(got2)
                return render(request, "search_course111.html", {"tok": tok, "got": cont, "got2": got2})

            except:
                return render(request, "search_course111.html", {"tok": tok, "cont": cont, "ck": False})
        else:
            cont = Video.objects.all()
            try:
                got = Video.objects.get(identification_code=tok)
                return render(request, "search_course111.html", {"tok": tok, "got": got, "ck": True})
            except:
                return render(request, "search_course111.html", {"tok": tok, "cont": cont, "ck": False})
    except:
        try:
            tok = None
            return render(request, "search_course111.html", {"tok": tok, "cont": cont, "ck": False})
        except:
            return HttpResponse("Your Search input was Empty")

def search_course11(request,tok):
        try:
            if request.method=="POST":
                tok=request.POST.get("qq")
                cont = Audio.objects.all()
                tok = tok.upper()
                got2 = None
                try:
                    got2 = []
                    for i in cont:
                        toU=str(i.title)
                        if tok == toU.upper():
                            got2.append(i.identification_code)
                    print(got2)
                    return render(request, "search_course11.html", {"tok": tok, "got": cont,"got2":got2})

                except:
                    return render(request, "search_course11.html", {"tok": tok, "cont": cont, "ck": False})
            else:
                cont=Audio.objects.all()
                try:
                    got = Audio.objects.get(identification_code=tok)
                    return render(request, "search_course11.html", {"tok": tok, "got": got, "ck": True})
                except:
                    return render(request, "search_course11.html", {"tok": tok, "cont": cont,"ck":False})
        except:
            try:
                tok=None
                return render(request, "search_course11.html", {"tok": tok, "cont": cont, "ck": False})
            except:
                return HttpResponse("Your Search input was Empty")




