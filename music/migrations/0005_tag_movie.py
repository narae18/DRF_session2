# Generated by Django 4.2.3 on 2023-07-11 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_rename_track_number_track_track_no'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('content', models.TextField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('tag', models.ManyToManyField(blank=True, to='music.tag')),
            ],
        ),
    ]
