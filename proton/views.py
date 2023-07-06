from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'proton/index.html')

def blog(request):
    return render(request, 'proton/blog.html')