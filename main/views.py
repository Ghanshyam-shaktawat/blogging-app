from unicodedata import category
from django.shortcuts import render
from django.views import generic
from pkg_resources import require
from .models import Category, Post
from .forms import PostForm, EditForm
from django.urls import reverse_lazy
from accounts.models import CustomUser
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.db.models import Q
from django.conf import settings
User = settings.AUTH_USER_MODEL

class IndexView(generic.ListView):
    """Shows the list view of all the blogs."""
    model = Post
    template_name = 'main/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_list'] = Post.objects.filter(status='p').order_by('-pub_date')
        context['featured_post'] = Post.objects.filter(status='p', featured=True).order_by('-pub_date')
        return context
    
class PostDetailView(generic.DetailView):
    """Shows the individual blog in detail."""
    model = Post
    template_name= 'main/post.html'

class AddPostView(generic.CreateView):
    """Add a new post view for our blog""" 
    model = Post
    form_class = PostForm
    template_name = 'main/add_post.html'
    
    def form_valid(self, PostForm):
        """Auto inserts the current logged user into the author field."""
        PostForm.instance.author = self.request.user
        return super().form_valid(PostForm)
 
class EditPostView(generic.UpdateView):
    """Update or edit the post by the author."""
    model = Post
    form_class = EditForm
    template_name = 'main/edit_post.html'
    success_url= "/{slug}"
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        post = self.get_object()
        if post.author != self.request.user:
            raise PermissionDenied
        
        return super(EditPostView, self).dispatch(request, *args, **kwargs)
  
class DeletePostView(generic.DeleteView):
    """Delete a post from the databsae."""
    model = Post
    template_name = 'main/delete_post.html'
    success_url= reverse_lazy('main:user-post')
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        post = self.get_object()
        if post.author != self.request.user:
            raise PermissionDenied
        
        return super(DeletePostView, self).dispatch(request, *args, **kwargs)

class AllPostByUserView(generic.ListView):
    model = Post
    template_name = 'main/your_post.html'
    
    def get_queryset(self):
        """arrange the post list in date by order, from new to old"""
        return Post.objects.filter(author=self.request.user).order_by('-pub_date')
    
    
class SearchPostView(generic.ListView):
    model = Post
    template_name="main/search.html"
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        if not query:
            raise Http404
        object_list = Post.objects.filter(Q(title__icontains=query) | Q(snippets__icontains=query), status='p')
        return object_list
    
def CategoryView(request, cats):
    try:
        category = Category.objects.get(cate=cats)
    except Category.DoesNotExist:
        raise Http404("Category does not exist")
    category_post = category.posts.all()
    return render(request, 'main/category.html', {'cats': cats, 'category_post':category_post})