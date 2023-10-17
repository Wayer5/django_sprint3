from datetime import date

from django.shortcuts import render, get_object_or_404

from blog.models import Post, Category

post_limit = 5


def get_posts_qs(model, **filter_fields):
    return Post.objects.all().filter(
        is_published=True, category__is_published=True,
        pub_date__lte=date.today(), **filter_fields)


def index(request):
    template = 'blog/index.html'
    posts = get_posts_qs(Post.objects)[:post_limit]
    context = {'post_list': posts, }
    return render(request, template, context)


def post_detail(request, id):
    template = 'blog/detail.html'
    post = get_object_or_404(
        get_posts_qs(Post.objects),
        id=id)
    context = {'post': post, }
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    category = get_object_or_404(
        Category.objects.filter(is_published=True), slug=category_slug)
    posts = Post.objects.all().filter(
        is_published=True, category__title=category,
        pub_date__lte=date.today())
    context = {'category': category, 'post_list': posts, }
    return render(request, template, context)
