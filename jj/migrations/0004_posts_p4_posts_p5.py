# Generated by Django 4.1.3 on 2022-11-22 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jj', '0003_posts'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='p4',
            field=models.CharField(default='', max_length=400),
        ),
        migrations.AddField(
            model_name='posts',
            name='p5',
            field=models.CharField(default='', max_length=400),
        ),
    ]
