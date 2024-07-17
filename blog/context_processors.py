from .models import Blog


def recent_posts(request):
    recent_posts = Blog.objects.order_by('-date')[:5]
    return {'recent_posts': recent_posts}
