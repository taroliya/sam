# Generated by Django 4.1.3 on 2022-11-22 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jj', '0006_event_p3_event_p4_alter_event_p1_alter_event_p2'),
    ]

    operations = [
        migrations.CreateModel(
            name='train',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image1', models.ImageField(upload_to='images')),
                ('image2', models.ImageField(upload_to='images')),
                ('image3', models.ImageField(default='', upload_to='images')),
                ('h1', models.CharField(default='', max_length=500)),
                ('h2', models.CharField(default='', max_length=500)),
                ('h3', models.CharField(default='', max_length=500)),
                ('p1', models.CharField(default='', max_length=400)),
                ('p2', models.CharField(default='', max_length=400)),
                ('p3', models.CharField(default='', max_length=400)),
                ('sh1', models.CharField(default='', max_length=200)),
                ('sh2', models.CharField(default='', max_length=200)),
                ('sh3', models.CharField(default='', max_length=200)),
            ],
        ),
    ]
