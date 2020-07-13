from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, 'home.html', {'hithere':'this is a dict'})


def contact(request):
    return HttpResponse('Contact information: asjhdajsdh')
