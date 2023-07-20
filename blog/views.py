from django.shortcuts import render, get_object_or_404
#importo el modelo Post
from .models import Post

# Create your views here.
def render_posts(request):
    posts = Post.objects.all()
    return render(request, 'posts.html', {'posts': posts})

#el post_id es el número de post que tipeo del post
def post_detail(request, post_id):
    #vamos a buscar en la base de datos un post que tenga el id que recibimos
    #almacenamos en post_id a todo el objeto post cuyo id es el que hemos recibido
    post = get_object_or_404(Post, pk=post_id)
    #retornamos la vista con el objeto post
    return render(request, 'post_detail.html', {'x': post})