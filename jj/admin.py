from django.contrib import admin
from jj.models import post
from jj.models import posts
from jj.models import event
from jj.models import train
# Register your models here.
admin.site.register(post)
admin.site.register(posts)
admin.site.register(event)
admin.site.register(train)