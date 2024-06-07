from django.http import HttpResponse
from django.template import loader

def index(request):
  template = loader.get_template('myfirst.html')
  return HttpResponse(template.render())

def about(request):
  template = loader.get_template('about.html')
  return HttpResponse(template.render())

def hello(request, first_name):
  return HttpResponse(f'Hello {first_name}')

def Sum(request, num1, num2):
  return HttpResponse(f"The Sum of two number is {num1 + num2}")
