from django.contrib import admin
#importo mi modelo
from .models import Post
# Register your models here.
admin.site.register(Post)