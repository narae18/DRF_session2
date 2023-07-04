from django.db import models


class Album(models.Model):
    id = models.AutoField(primary_key=True,  null=False, blank=False)
    artist = models.CharField(max_length=100, null=False, blank=False)
    title = models.CharField(max_length=100, null=False, blank=False)
    released_at = models.IntegerField(null=False, blank=False)
    description = models.TextField(max_length=200, null=False, blank=False)
    
    def __str__(self):
        return self.title


class Track(models.Model):
    
    id = models.AutoField(primary_key=True, null=False, blank=False)
    track_number = models.SmallIntegerField(null=False, blank=False)
    track_title = models.CharField(null=False, blank=False, max_length=30)
    album_bonus = models.ManyToManyField(Album, related_name='tracks', max_length=30, blank=False)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null=True, blank=True, related_name='bonus')

    def __str__(self):
        return self.title
