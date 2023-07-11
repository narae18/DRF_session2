from rest_framework import serializers
from .models import *


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ['id', 'track_no', 'track_title']
        read_only_fields = ['album']


class AlbumSerializer(serializers.ModelSerializer):
    tracks = TrackSerializer(many=True, read_only=True)



    def get_tracks(self, instance):
        return instance.tracks.all()


    class Meta:
        model = Album
        fields = '__all__'
    
    tag = serializers.SerializerMethodField()    
    def get_tag(self,instance):
        tags = instance.tag.all()
        return [tag.name for tag in tags] 

        
    image = serializers.ImageField(use_url=True, required=False)



class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


