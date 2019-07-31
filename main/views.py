from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.utils import timezone

from .forms import PostForm
from .models import Post

def home(request):
    posts = Post.objects.order_by('-date')

    context = {
        'posts' : posts,
    }

    return render(request, 'home.html', context)

def search(request):
    word = request.GET.get('q')
    
    searched_post = Post.objects.filter(Q(title__icontains = word))
   
    context = {
        'posts' : searched_post,
    }
    return render(request, 'search.html', context)    

def new(request):
    return render(request, 'new.html')

def create(request):
    post = Post()

    post.title = request.POST['title']
    post.body = request.POST['body']

    post.save()

    return redirect('/')

def detail(request, post_id):
    posts = get_object_or_404(Post, pk = post_id)

    context = {
        'posts' : posts,
    }

    return render(request, 'detail.html', context)

def delete(request, post_id):
    posts = get_object_or_404(Post, pk = post_id) #객체를 받아오는 부분
    posts.delete() #객체의 method로 객체를 삭제하고 db에 저장
   
    return redirect('/')

def edit(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
    
        if form.is_valid():
            post = form.save(commit=False)
            # 저장하기전 상태의 데이터값을 자동으로 form에 채워줌
            post.save()
            return redirect('/')
    else:
        form = PostForm(instance=post)
    
    return render(request, 'update.html', {'form': form})
