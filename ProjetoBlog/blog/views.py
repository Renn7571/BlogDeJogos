from django.shortcuts import render, redirect
# Create your views here.
from django.http import HttpResponse

from .models import post, comentario

def login(request): 
    return render(request, 'login.html', {})

def home (request):
    posts = post.objects.all()
    #for post in posts:
    #    post.img.url = '/teste/' + post.img.url
    return render(request, 'home.html', {'posts': posts})

def post_details(request, slug):
    posts = post.objects.get(slug=slug)

    if request.method =='POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        conteudo = request.POST.get('conteudo')
        comentarionovo = comentario(nome=nome, email=email, conteudo=conteudo, posts=posts) # Associa o comentario ao post
        comentarionovo.save() # Salva o comentario no banco
        # return redirect('post_details.html', slug=post.slug) # Quando enviar o comentario reseta a pagina

    return render(request, 'post_details.html', {'post': posts})

