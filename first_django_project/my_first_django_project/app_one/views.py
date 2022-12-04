from django.shortcuts import render, HttpResponse, redirect

from django.http import JsonResponse

def root(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def index(request):
    return HttpResponse('placeholder to display a new form to create a new blog, part two')

def new(request):
    return HttpResponse('placeholder to display a new form to create a new blog, part three')
    
def create(request):
    return redirect('/')

def show(request, num):
    # number = num
    # return HttpResponse('placeholder to display blog number'+""+number)
    number={
        'blog_number':num
    }
    return render(request, 'test.html',number)

def edit(request, num):
    number=num
    return HttpResponse('placeholder to edit blog'+" "+number)

def destroy(request, num):
    return redirect('/')

def redirected_method(request):
    return JsonResponse({"response": "Title: 'My first blog' content: 'Lorem, ipsum dolor sit amet'", "status":True})
