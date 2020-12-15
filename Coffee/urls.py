from django.urls import path

from . import views

app_name = 'Coffee'
urlpatterns = [
    path('', views.index, name='index'),
    path('recipe/', views.recipe_home, name='recipeHome'),
    path('recipe/<int:recipe_id>/', views.recipe, name='recipe'),
    path('recipe/<int:recipe_id>/like', views.recipe_like, name='recipeLike'),
    path('recipe/<int:recipe_id>/comment', views.recipe_comment, name='recipeComment'),
    path('written/', views.written_home, name='writtenPieceHome'),
    path('written/<int:written_id>/', views.written, name='writtenPiece'),
    path('written/<int:written_id>/like', views.written_like, name='writtenPieceLike'),
    path('written/<int:written_id>/comment', views.written_comment, name='writtenPieceComment')
]
