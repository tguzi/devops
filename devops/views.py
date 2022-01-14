from django.http import HttpResponse
from django.shortcuts import render

def index (request):
  context = {}
  print(request.body)
  context['hello'] = 'hello world'
  return render(request, 'index.html', context)
  # return HttpResponse("Hello World!", request)