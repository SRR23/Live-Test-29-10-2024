from django.shortcuts import render, redirect
from .import forms
from .import models
from django.db.models import Q

def add_post(request):
    if request.method == 'POST':
        post_form = forms.PostForm(request.POST)
        if post_form.is_valid():
            post_form.save()
            return redirect('add_post')
        
    else:
        post_form = forms.PostForm()
        
    return render(request, 'add_post.html',{'form': post_form})


def edit_post(request, id):
    post = models.Post.objects.get(pk=id)
    post_form = forms.PostForm(instance=post)
    if request.method == 'POST':
        post_form = forms.PostForm(request.POST)
        if post_form.is_valid():
            post_form.save()
            return redirect('add_post')
        
    else:
        post_form = forms.PostForm()
        
    return render(request, 'add_post.html',{'form': post_form})

def delete_post(request, id):
    post = models.Post.objects.get(pk=id)
    post.delete()
    
    return redirect ('homepage')


def search_blogs(request):
    search_key = request.GET.get('search', None)
    
    
    if search_key:
        blogs = models.Post.objects.filter(
            Q(title__icontains=search_key) |
            Q(category__title__icontains=search_key)
        ).distinct()

        context = {
            "blogs": blogs,
            "search_key": search_key
        }

        return render(request, 'search_blogs.html', context)

    else:
        return redirect('home')