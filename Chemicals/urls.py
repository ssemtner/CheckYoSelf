from django.urls import path

from . import views

app_name = 'Chemicals'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:topic_id>/', views.detail, name='detail'),
    path('<int:topic_id>/like/<int:group_id>/', views.like, name='like'),
]
