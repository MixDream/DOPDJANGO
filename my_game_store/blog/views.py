from django.shortcuts import render
from my_game_store.blog.models import Post
from django.core.paginator import Paginator

def post_list(request):
    post_list = Post.objects.all().order_by('-published_date')
    paginator = Paginator(post_list, 5)  # 5 постов на страницу
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/post_list.html', {'page_obj': page_obj})
