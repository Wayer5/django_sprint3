from django.shortcuts import render, get_object_or_404
from blog.models import Post
from blog.models import Category
from datetime import date


def index(request):
    template = 'blog/index.html'
    post_list = Post.objects.all().filter(
        is_published=True, category__is_published=True,
        pub_date__lte=date.today())[0:5]
    context = {'post_list': post_list, }
    return render(request, template, context)


def post_detail(request, id):
    template = 'blog/detail.html'
    post = get_object_or_404(
        Post.objects.filter(
            is_published=True,
            category__is_published=True,
            pub_date__lte=date.today()),
        id=id)
    context = {'post': post, }
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    category = get_object_or_404(
        Category.objects.filter(is_published=True), slug=category_slug)
    post_list = Post.objects.all().filter(
        is_published=True, category__title=category,
        pub_date__lte=date.today())
    context = {'category': category, 'post_list': post_list, }
    return render(request, template, context)
