from django.shortcuts import render
from .models import Article, Tag
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.conf import settings
from .forms import NameForm

# Create your views here.
from datetime import datetime
def home(request):#主页
    a = Article.objects.all()
    paginator = Paginator(a, settings.PAGE_NUM)
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)
    return render(request, 'blog/home.html', {'post_list':post_list})

def detail(request, id): #查看文章详情
    try:
        post = Article.objects.get(id = str(id))
        post.viewed() # 更新游览次数
        tags = post.tags.all() #获取文章对应的所有标签
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'blog/post.html', {'post':post,'tags':tags})



