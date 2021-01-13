from django.urls import path

from . import views

app_name = 'Elements'
urlpatterns = [
    path('', views.index, name='index')
]
