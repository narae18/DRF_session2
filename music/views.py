from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Album, Track
from .serializers import AlbumSerializer, TrackSerializer


from django.shortcuts import get_object_or_404


@api_view(['GET', 'POST', 'PATCH', 'DELETE'])
def album_list(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    if request.method == 'GET':
        serializer = AlbumSerializer(album)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AlbumSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'PATCH':
        serializer = AlbumSerializer(instance=album, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'DELETE':
        album.delete()
        data = {
            'deleted album': album_id
        }
        return Response(data)


@api_view(['GET', 'POST', 'PATCH', 'DELETE'])
def track_list(request, track_id):
    if request.method == 'GET':
        tracks = Track.objects.all()
        serializer = TrackSerializer(tracks, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TrackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'PATCH':
        track = get_object_or_404(Track, id=track_id)
        serializer = TrackSerializer(instance=track, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'DELETE':
        track = get_object_or_404(Track, id=track_id)
        track.delete()
        data = {
            'deleted_track': track_id
        }
        return Response(data)