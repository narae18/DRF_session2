# Generated by Django 4.2.3 on 2023-07-11 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0005_tag_movie'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='tags',
            field=models.ManyToManyField(blank=True, to='music.tag'),
        ),
        migrations.DeleteModel(
            name='Movie',
        ),
    ]
