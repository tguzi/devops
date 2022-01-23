from django.http import HttpResponse
from django.shortcuts import render

def index (request):
  print(request.body)
  return render(request, 'index.html')
  # return HttpResponse("Hello World!", request)