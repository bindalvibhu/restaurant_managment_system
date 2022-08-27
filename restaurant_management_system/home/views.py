from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, 'homepage.html')

def about(request):
    return HttpResponse('about page')
