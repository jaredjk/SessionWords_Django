from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime #from seconds since the epoch, struct_time in UTC, use gmtime()

def index(request):
    print strftime("%Y-%m-%d %H:%M:%S", gmtime())
    return render(request, 'sessionwords_app/index.html')

def add_word(request):
    if request.method == "POST":
        if not 'wordinput' in request.session: 
            request.session['wordinput'] = []
        else:
            request.session['wordinput'] = request.session['wordinput']
        temp = {
            'word':request.POST['input_word'],
            'color':request.POST['color'],
            'font':request.POST['big_font'],
            'time':strftime ("%Y-%m-%d %H:%M:%S", gmtime())
            }
        request.session['wordinput'].append(temp)
        return redirect("/")
    else:
        return redirect("/")

def clear(request):
    request.session['wordinput'] = []
    return redirect('/')






