from django.contrib import admin
# pylint: disable=relative-beyond-top-level
from .models import Post, Pizza

# Register your models here.
admin.site.register(Post)
admin.site.register(Pizza)
