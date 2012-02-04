from django.shortcuts import render
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from solo.models import Post


def page(request, page_number=False, slug=False):
    """
    Return a paginated list of articles.
    """
    if slug:
        posts = Post.objects.filter(slug=slug)
        posts_per_page = 1
    else:
        posts = Post.objects.filter(public=True)
        posts_per_page = 10
    paginator = Paginator(posts, posts_per_page)

    try:
        page = int(page_number)
    except ValueError:
        page = 1

    try:
        some_posts = paginator.page(page)
    except (EmptyPage, InvalidPage):
        some_posts = paginator.page(paginator.num_pages)

    return render(request, 'posts.html', {'posts': some_posts})


def detail(request, slug):
    """
    Returns a single article view
    """
    return page(request, 1, slug)
