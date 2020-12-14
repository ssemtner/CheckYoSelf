from django.urls import path

from . import views

app_name = 'Coffee'
urlpatterns = [
    path('', views.index, name='index'),
    path('artwork/', views.artwork_home, name='artworkHome'),
    path('artwork/<int:artwork_id>/', views.artwork, name='artwork'),
    path('artwork/<int:artwork_id>/like', views.artwork_like, name='artworkLike'),
    path('artwork/<int:artwork_id>/comment', views.artwork_comment, name='artworkComment'),
    path('written/', views.written_home, name='writtenPieceHome'),
    path('written/<int:written_id>', views.written, name='writtenPiece'),
    path('written/<int:written_id>/like', views.written_like, name='writtenPieceLike'),
]
