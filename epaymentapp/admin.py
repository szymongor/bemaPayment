from django.contrib import admin
from .models import Post, SiteUser, Bill

admin.site.register(SiteUser)
admin.site.register(Post)
admin.site.register(Bill)
