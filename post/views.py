from django.shortcuts import render
from django.views.generic import ListView , DetailView , CreateView , UpdateView , DeleteView
# Create your views here.
from .models import Post 



class PostList(ListView):
    model = Post  ## in template [ object_list , post_list ]
    # context_object_name = 'all_posts'
    ordering = ['-created_at']
    # queryset = Post.objects.filter(active=True)
    # template_name = 'post/test.html'

    def get_queryset(self):
        return Post.objects.filter(active=True)
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['myname'] = 'mahmmoud ahmed'
        context['lastname'] = 'python developer'
        return context



class PostDetail(DetailView):
    model = Post



class PostCreate():
    pass



class PostDelete():
    pass




class PostUpdate():
    pass
