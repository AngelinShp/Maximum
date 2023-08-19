from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
# прописываем, что можно вернуть на к-нибудь запрос
from django.urls import reverse
from .forms import AdvertisementForm
from .models import Advertisement


def index(request):
    advertisements=Advertisement.objects.all()
    context={'advertisements': advertisements}
    return render(request, 'index.html', context)
def top_sellers(request):
    return render(request, 'top-sellers.html')
def advertisement_post(request):
    if request.method=='POST':
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            advertisement=Advertisement(**form.cleaned_data)
            advertisement.user=request.user
            advertisement.save()
            url=reverse('main-page')
            return redirect(url)
    else:
        form=AdvertisementForm()
    context={'form':form}
    return render(request, 'advertisement-post.html', context)
