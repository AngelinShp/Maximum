from .views import dz_index
from django.urls import path

urlpatterns=[
    path('lesson_4', dz_index)
]