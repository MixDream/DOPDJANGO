from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Buyer, Game
def index(request):
    return render(request, 'index.html')
def games_list(request):
    games = Game.objects.all()
    return render(request, 'games.html', {'games': games})
def cart(request):
    return render(request, 'cart.html')
def registration(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not Buyer.objects.filter(name=username).exists():
            Buyer.objects.create(name=username, balance=0.0, age=18)
            return redirect('index')
    return render(request, 'registration.html')
from django.shortcuts import render
from .models import Post

def create_posts(request):
    Post.objects.create(title='Первая статья', content='Содержание первой статьи', published_date='2024-01-01')
    Post.objects.create(title='Вторая статья', content='Содержание второй статьи', published_date='2024-02-01')
    Post.objects.create(title='Третья статья', content='Содержание третьей статьи', published_date='2024-03-01')
    return render(request, 'task1/posts_created.html')
def update_post(request, post_id):
    post = Post.objects.get(id=post_id)
    post.title = 'Новый заголовок'
    post.save()
    return render(request, 'task1/post_updated.html', {'post': post})
def list_posts(request):
    all_posts = Post.objects.all()
    return render(request, 'task1/list_posts.html', {'posts': all_posts})
def delete_post(request, post_id):
    post_to_delete = Post.objects.get(id=post_id)
    post_to_delete.delete()
    return render(request, 'task1/post_deleted.html')
def filter_posts(request):
    posts_2024 = Post.objects.filter(published_date__year=2024)
    return render(request, 'task1/filter_posts.html', {'posts': posts_2024})
