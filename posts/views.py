from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm


def like(request, post_id):
    like = Post.objects.get(id = post_id)
    like.likes +=1 
    like.save()
    return HttpResponseRedirect('/')

def index(request):
    if request.method=='POST':
        form= PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

        else:
            return HttpResponseRedirect(form.errors.as_json())    
    posts = Post.objects.all()[:20]

    return render(request, 'posts.html',
              {'posts': posts})

def delete(request, post_id):
    post = Post.objects.get(id = post_id)
    post.delete()
    return HttpResponseRedirect('/')

def edit(request, post_id):
    posts= Post.objects.get(id=post_id)
    if request.method=="GET":
        return render(request,'edit.html',{'posts':posts})
    if request.method=='POST':
        posts=Post.objects.get(id=post_id)
        form= PostForm(request.POST, request.FILES,instance=posts)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

        else:
            return HttpResponseRedirect("not valid")
    