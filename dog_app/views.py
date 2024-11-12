from django.shortcuts import render

# Create your views here.
def home(request):
    """ display home page"""
    return render(request, 'index.html')

def contact(request):
    """ dispaly contact page"""
    context = {}
    return render(request, 'contact.html', context)
