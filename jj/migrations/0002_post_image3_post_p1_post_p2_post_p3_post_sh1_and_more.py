# Generated by Django 4.1.3 on 2022-11-18 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jj', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image3',
            field=models.ImageField(default='', upload_to='images'),
        ),
        migrations.AddField(
            model_name='post',
            name='p1',
            field=models.CharField(default='', max_length=400),
        ),
        migrations.AddField(
            model_name='post',
            name='p2',
            field=models.CharField(default='', max_length=400),
        ),
        migrations.AddField(
            model_name='post',
            name='p3',
            field=models.CharField(default='', max_length=400),
        ),
        migrations.AddField(
            model_name='post',
            name='sh1',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='post',
            name='sh2',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='post',
            name='sh3',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='post',
            name='title1',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='post',
            name='title2',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='post',
            name='title3',
            field=models.CharField(default='', max_length=500),
        ),
    ]
