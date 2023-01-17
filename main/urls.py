from django.urls import path, re_path
from . import views
from .views import AddPostView, IndexView, PostDetailView, EditPostView, DeletePostView, AllPostByUserView, SearchPostView, CategoryView
from django.contrib.auth.decorators import login_required

app_name = 'main'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('category/<slug:cats>/', CategoryView, name='category'),
    path('search/', SearchPostView.as_view(), name='search'),
    path('add-post/', login_required(AddPostView.as_view()), name='add-post'),
    path('my/posts/', login_required(AllPostByUserView.as_view()), name='your-post'),
    path('<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
    path('edit/post/<slug:slug>/', login_required(EditPostView.as_view()), name='edit-post'),
    path('delete/post/<slug:slug>/', login_required(DeletePostView.as_view()), name='delete-post'),
]