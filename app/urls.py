from django.urls import path
from .views import post,postview,post_detail_view
urlpatterns = [
    path('post/',post , name = 'post'),
    path('postview/',postview , name = 'postview'),
    path('posts/<int:id>/', post_detail_view, name='post_detail_view'),
    
]