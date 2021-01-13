from django.urls import path

from . import views

app_name = 'Elements'
urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:element_name>/', views.detail, name='detail')
]
