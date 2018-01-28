from django.contrib import admin
from .models import Post, SiteUser

admin.site.register(SiteUser)
admin.site.register(Post)