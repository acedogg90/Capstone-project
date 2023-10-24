from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def restaurant(request):
    return render(request, 'restaurant_template.html')