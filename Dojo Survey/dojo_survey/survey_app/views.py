from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'index.html')

def process(request):
    name_from_form = request.POST['name']
    location_from_form = request.POST['location']
    favlanguage_from_form = request.POST['favlanguage']
    comment_from_form = request.POST['comment']
    context = {
        "name_on_template": name_from_form,
        "location_on_template": location_from_form,
        "favlanguage_on_template": favlanguage_from_form,
        "comment_on_template": comment_from_form
    }
    return render(request, "result.html", context)

def result(request):
    return render(request, "result.html")

def back(request):
    return redirect('/')