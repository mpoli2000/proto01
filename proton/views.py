from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'proton/index.html')

def blog(request):
    return render(request, 'proton/blog.html')

def blog_details(request):
    return render(request, 'proton/blog-details.html')

def services_details(request):
    return render(request, 'proton/services-details.html')

def portfolio_details(request):
    return render(request, 'proton/portfolio-details.html')