from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

def homepage(request):
    
    context = {
        
    }
    return render(request, 'main/home.html', context)