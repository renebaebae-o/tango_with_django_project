from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}

    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    return HttpResponse("This tutorial has been put together by Yufei Wang. <br/><a href='/rango/'>Home</a>")