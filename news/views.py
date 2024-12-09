from django.shortcuts import render
from django.core.paginator import Paginator
from news.models import CreatePost


def posting_news(request):
    posts = CreatePost.objects.all().order_by('-created_at')
    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'news.html', {'page_obj': page_obj})
# Create your views here.

#python manage.py makemigrations
