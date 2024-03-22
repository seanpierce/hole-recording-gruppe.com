
from django.shortcuts import render 

 
def index(request):
    context = {
        'title': 'hole recording gruppe'
    }
    
    return render(request, 'index.html', context)