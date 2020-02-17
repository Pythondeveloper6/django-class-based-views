from django.shortcuts import render

# Create your views here.
from .models import Post


def post_list(request):
    post_list = Post.objects.all()
    return render(request , 'post/list.html',{'post_list' : post_list})


def post_detail(request , id):
    pass