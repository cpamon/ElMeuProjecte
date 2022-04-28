from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('this is the shop')

def shop(request):
    template = 'shop.html'
    context = {'elMeuText': 'Contingut del text'}
    return render(request, template, context)