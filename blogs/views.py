from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.decorators import login_required
from django.utils.datastructures import MultiValueDictKeyError


@login_required
def blogs(request):
    blogs = reversed(Blog.objects.all())
    return render(request, 'blogs/index.html', {'blogs': blogs})

@login_required
def create_blog(request):
    # todo send email to all followers
    if request.method == 'POST':
        try:
            blog = Blog(
                title=request.POST['title'],
                body=request.POST['body'],
                author=request.user,
                image=request.FILES['image']
            )
        except MultiValueDictKeyError:
            return 
        else:
            blog.save()

        return redirect('/')

@login_required
def delete_blog(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if blog.author == request.user:
        blog.image.delete(save=True)
        blog.delete()
    return redirect('/')


def add_comment(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)

    # todo: send email to the blog author
    new_comment = Comment(
        blog=blog,
        comment_by=request.user,
        body=request.POST['body']
    )

    new_comment.save()
    return redirect('/')