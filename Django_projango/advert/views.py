from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
# прописываем, что можно вернуть на к-нибудь запрос
from django.urls import reverse, reverse_lazy
from .forms import AdvertisementForm
from .models import Advertisement


def index(request):
    advertisements=Advertisement.objects.all()
    context={'advertisements': advertisements}
    return render(request, 'advert/index.html', context)
def top_sellers(request):
    return render(request, 'advert/top-sellers.html')

@login_required(login_url=reverse_lazy('login'))
def advertisement_post(request):
    if request.method == "POST":
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            new_advertisement = form.save(commit=False)
            new_advertisement.user = request.user
            new_advertisement.save()
            url = reverse('main-page')
            return redirect(url)
    else:
        form = AdvertisementForm()
    context = {'form': form}
    return render(request, 'advert/advertisement-post.html', context)