from django.urls import path
from . import views

app_name = 'proton'
urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.blog, name='blog'),
    
]