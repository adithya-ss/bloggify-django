from django.contrib import admin
from .models import Post, Category, Comment

#Registering the posts into the admin area for creation/updation/deletion.
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)