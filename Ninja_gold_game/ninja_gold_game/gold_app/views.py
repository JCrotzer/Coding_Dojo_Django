from django.shortcuts import render, redirect
import random
from time import localtime, strftime

# Create your views here.

def index(request):
    if 'counter' not in request.session:
        request.session['counter'] = 0
    if 'activities' not in request.session:
        request.session['activities'] = []
    return render(request, "index.html")

def gold(request):
    #If hidden input equals "farm", generate random integer between 10-20
    if request.POST['property'] == 'farm':
        gold = random.randint(10,20)
        request.session['activities'].append('Earned' + ' ' + str(gold) + ' ' + 'gold from the' + ' ' + request.POST['property'] + '!' + '' + '(' + str(strftime("%Y %m %d %I:%M %p", localtime())) + ')')
        request.session['counter'] += gold
    #If hidden input equals "cave", generate random integer between 5-10
    elif request.POST['property'] == 'cave':
        gold = random.randint(5,10)
        request.session['activities'].append('Earned' + ' ' + str(gold) + ' ' + 'gold from the' + ' ' + request.POST['property'] + '!' + '' + '(' + str(strftime("%Y %m %d %I:%M %p", localtime())) + ')')
        request.session['counter'] += gold
    #If hidden input equals "house", generate random integer between 2-5
    elif request.POST['property'] == 'house':
        gold = random.randint(2,5)
        request.session['activities'].append('Earned' + ' ' + str(gold) + ' ' + 'gold from the' + ' ' + request.POST['property'] + '!' + '' + '(' + str(strftime("%Y %m %d %I:%M %p", localtime())) + ')')
        request.session['counter'] += gold
    #If hidden input equals "casino", generate random integer between -50-50.
    elif request.POST['property'] == 'casino':
        gold = random.randrange(-50,50)
        #if random integer is less than or equal to 0, have activities display gold lost in red
        if gold < 0:
            request.session['activities'].append('Entered a casino and lost' + ' ' + str(gold) + ' ' + 'gold.' + ' ' + 'Ouch...' + ' ' + '(' + str(strftime("%Y %m %d %I:%M %p", localtime())) + ')')
            request.session['counter'] += gold
        #if random integer is greater than 0, have activities display gold won in red
        else:
            request.session['activities'].append('Entered a casino and won' + ' ' + str(gold) + ' ' + 'gold.' + ' ' + 'Yay!!!...' + '(' + str(strftime("%Y %m %d %I:%M %p", localtime())) + ')')
            request.session['counter'] += gold
    return redirect('/')

def reset(request):
    del request.session['counter']
    del request.session['activities']
    return redirect('/')