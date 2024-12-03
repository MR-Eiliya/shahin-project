from django.shortcuts import render, get_object_or_404
from blog.models import Post, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.forms import CommentForm
from django.contrib import messages
#from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect




#@login_required(login_url="/accounts/login")
def blog_view(request,**kwargs):
    posts = Post.objects.filter(status=1)
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name = kwargs['cat_name'])  
    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username = kwargs['author_username'])
    if kwargs.get('tag_name') != None:
        posts = posts.filter(tags__name__in=[kwargs['tag_name']])    
    posts = Paginator(posts,3)
    try:
        page_number = request.GET.get('page')   
        posts = posts.get_page(page_number)
    except PageNotAnInteger or EmptyPage:
        posts = posts.get_page(1)
    context = {'posts':posts}
    return render(request, 'blog/blog-home.html',context)

        
def blog_single(request,pid):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request,'دیدگاه شما با موفقیت ارسال و مورد تایید قرار گرفت!')
        else:
            messages.error(request,'ثبت دیدگاه با خطا مواجهه شد!')
    
    posts = Post.objects.filter(status=1)
    post = get_object_or_404(posts,pk=pid,status=1) 
    post.counted_view = post.counted_view + 1
    comments = Comment.objects.filter(post=post.id,approved=True)
    form = CommentForm()
    context = {'post':post,'comments':comments,'form':form}
    
    return render(request, 'blog/blog-single.html',context)
        

def blog_category(request,cat_name):
    posts = Post.objects.filter(status=1) 
    posts = posts.filter(category__name=cat_name)
    cat_count = posts.objects.filter(category__name=cat_name).count()
    context = {'posts':posts,'cat_count':cat_count}
    return render(request, 'blog/blog-single.html',context)



    

   
        
