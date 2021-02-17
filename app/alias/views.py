from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('all is ok')


def get_by_slug(request):
    pass
    #return render()