from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def dz_index(request):
    return HttpResponse('Домашка по 4 занятию')
