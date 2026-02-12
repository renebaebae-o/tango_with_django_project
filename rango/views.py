from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Rango says hey there partner! <br/><a href='/rango/about/'>About</a>")
def about(request):
    return HttpResponse("This tutorial has been put together by Yufei Wang. <br/><a href='/rango/'>Home</a>")