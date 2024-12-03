from django import template
from blog.models import Post, Category
from django.utils import timezone


register = template.Library()

'''@register.inclusion_tag('blog/latest-post.html')
def latestpost(arg=3):
    posts = Post.objects.filter(status=1).order_by('published_date')[:arg]
    return {'posts':posts}'''

@register.inclusion_tag('blog/post-categories.html')
def postcategories():
    posts = Post.objects.filter(status=1)
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name] = posts.filter(category=name).count()
    return {'categories':cat_dict}

@register.inclusion_tag('website/latest-post.html')
def index_latest_posts(arg=3):
    now = timezone.now()
    posts = Post.objects.filter(status=1,published_date__lte = now).order_by('-published_date')[:arg]
    return {'posts':posts}

@register.inclusion_tag('blog/single-recents.html')
def sidebar_recent_posts(arg=4):
    now = timezone.now()
    posts = Post.objects.filter(status=1,published_date__lte = now).order_by('-published_date')[:arg]
    return {'posts':posts}
    
