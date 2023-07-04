from django.urls import path
from . import views

app_name='music'
urlpatterns = [
    path('', views.album_list, name='album_list'),
    path('<int:album_id>/album', views.album_list, name='album_detail'),
    path('tracks/', views.track_list),
    path('<int:track_id>/tracks', views.track_list),
]

