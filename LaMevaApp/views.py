from django.shortcuts import render
from django.http import HttpResponse
from .models import Animals

# Create your views here.
def index(request):
    return HttpResponse('HelloWorld!')

def about(request):
    llistaAnimals = Animals.objects.all()
    template = 'template1.html'
    context = {'elMeuText': 'Contingut del text', 'llistaAnimals': llistaAnimals}
    return render(request, template, context)