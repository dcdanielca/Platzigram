from django.urls import path
from posts import views 

urlpatterns = [

    path(
        route = 'posts/<int:id>/',
        view = views.PostDetailView.as_view(),
        name = 'detail'
    ),

    path(
        route = '', 
        view = views.PostFeedView.as_view(), 
        name='feed'
    ),
    path(
        route = 'posts/', 
        view = views.PostFeedView.as_view(), 
        name = 'feed'
    ),
    path(
        route = 'posts/new/', 
        view = views.CreatePostView.as_view(), 
        name = 'create'
    ),
]
    