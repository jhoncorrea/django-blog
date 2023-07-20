from django.urls import path
from .views import render_posts, post_detail

# es una característica útil para evitar conflictos de nombres de URL cuando tienes múltiples aplicaciones en tu proyecto Django.
app_name = 'blog'

urlpatterns = [
    path('', render_posts, name='posts'),
    path('<int:post_id>', post_detail, name='post_detail'),
]