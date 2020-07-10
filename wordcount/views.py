from django.http import HttpResponse


def homepage(request):
    return HttpResponse('Hello')


def contact(request):
    return HttpResponse('Contact information: asjhdajsdh')
