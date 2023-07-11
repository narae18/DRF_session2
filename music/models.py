from django.db import models

#태그가 바로 위에있어야인식
def image_upload_path(instance,filename):
    return f'{instance.id}/{filename}'

class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    


class Album(models.Model):
    id = models.AutoField(primary_key=True,  null=False, blank=False)
    artist = models.CharField(max_length=100, null=False, blank=False)
    title = models.CharField(max_length=100, null=False, blank=False)
    released_at = models.IntegerField(null=False, blank=False)
    description = models.TextField(max_length=200, null=False, blank=False)
    tag = models.ManyToManyField(Tag, blank=True)
    image = models.ImageField(upload_to='images_upload_path', null=True, blank=True)
    
    def __str__(self):
        return self.title


class Track(models.Model):
    
    id = models.AutoField(primary_key=True, null=False, blank=False)
    track_no = models.SmallIntegerField(null=False, blank=False)
    track_title = models.CharField(null=False, blank=False, max_length=30)
    
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null=True, blank=True, related_name='bonus')


    album_bonus = models.ManyToManyField(Album, related_name='tracks', max_length=30, blank=False)  



    def __str__(self):
        return self.title




