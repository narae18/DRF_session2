from django.urls import path
from .views import *
from . import views

app_name="music_app"
urlpatterns = [
    path('album/', views.album_list_create),
    path('<int:album_id>/track', views.track_list_create),
    path('album/<int:album_id>',views.album_detail_update_delete),
    path('track/<int:track_id>',views.track_detail_update_delete),
]