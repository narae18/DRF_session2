# Generated by Django 4.2.3 on 2023-07-11 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0007_rename_tags_album_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images_upload_path'),
        ),
    ]
