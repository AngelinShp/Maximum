from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# прописываем, что можно вернуть на к-нибудь запрос
def index(request):
    return HttpResponse('Успешно :)')