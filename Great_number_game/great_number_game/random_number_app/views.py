from django.shortcuts import render, redirect
import random

# Create your views here.
def index(request):
    if 'random' not in request.session:
        request.session['message'] = ""
        request.session['random'] = random.randrange(1, 101)
        print(request.session['random'])
    return render(request, 'index.html')

def guess(request):
    if request.session['random'] == int(request.POST['guess']):
        request.session['message'] = "correct"

    if request.session['random'] < int(request.POST['guess']):
        request.session['message'] = "high"

    if request.session['random'] > int(request.POST['guess']):
        request.session['message'] = "low"
    return render(request, "index.html")

def reset(request):
    del request.session['message']
    del request.session['random']
    return redirect('/')