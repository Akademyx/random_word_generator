from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    if not 'random' in request.session:
        request.session['random'] = get_random_string(length=14)
    else:
        request.session['random'] = get_random_string(length=14)
    
    if not 'count' in request.session:
        request.session['count'] = 0
    else:
        request.session['count'] += 1
    print request.session['count']
    context = {
        'count': request.session['count'],
        'random': request.session['random'] 
    }
    return render(request, 'index.html', context)

def process(request):
    print request.session['random']
    return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')