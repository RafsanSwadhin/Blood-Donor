from django.urls import path
from .views import post,postview,post_detail_view,filtered_post_view
urlpatterns = [
    path('post/',post , name = 'post'),
    path('postview/',postview , name = 'postview'),
    path('posts/<int:id>/', post_detail_view, name='post_detail_view'),
    path('post/filter/', filtered_post_view, name='filtered_post_view'),
    
]