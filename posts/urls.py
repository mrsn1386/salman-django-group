from django.urls import path

from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='all_posts'),
    path('create_post/', views.CreatePostView.as_view(), name='create_post'),
    path('my-posts/', views.MyPostsListView.as_view(), name='my_posts'),
    #path('my-profile/', views.ProfileView.as_view(), name='my_profile'),
]