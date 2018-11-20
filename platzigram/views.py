from django.http import HttpResponse
from datetime import datetime
from django.http import JsonResponse

def hello_world(request):
    now = datetime.now().strftime("%b, %dth, %Y -%H:%M hrs")
    return HttpResponse("Oh hi!, Current server time is {}".format(now))


def sort_integers(request):
    # import pdb;pdb.set_trace()
    numbers = sorted([int(i) for i in request.GET['numbers'].split(',')])
    return JsonResponse(numbers, safe=False)

def say_hi(request, name, age):
    if age < 12:
        message = 'Sorry {}, you are not allowed here'.format(name)
    else:
        message= 'Hello {}, Welcome to Platzigram'.format(name)   
    return HttpResponse(message)