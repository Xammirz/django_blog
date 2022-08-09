
from django.urls import path
from . import views
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('news/', views.NewsView.as_view(), name='news'),
    path('news/<slug:url>/', views.post_category, name='post_category'),
    path('new/<int:pk>/', views.DetailNewsView.as_view(), name='new_detail'),
    path('mynews/', views.AuthorNews.as_view(), name='mynews'),
    path('post/create', views.CreatePost.as_view(), name='new_post'),
    path('post/update/<int:pk>', views.UpdatePost.as_view(), name='update_post'),
    path('post/delete/<int:pk>', views.DeletePost.as_view(), name='delete_post'),
]
