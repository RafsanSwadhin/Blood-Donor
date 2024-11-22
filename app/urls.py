from django.urls import path
from .views import post,postview
urlpatterns = [
    path('post/',post , name = 'post'),
    path('postview/',postview , name = 'postview'),
    
]