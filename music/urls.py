from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from .views import *
from . import views

app_name="music_app"
urlpatterns = [
    path('album/', views.albumlist),
    path('<int:album_id>/track', views.tracklist),
    path('album/<int:album_id>',views.album_UD),
    path('track/<int:track_id>',views.track_UD),
    path('tag/<str:tag_name>',views.find_tag),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)